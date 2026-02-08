#!/usr/bin/env python3
"""
Download PDFs and extract images for all publications.

Usage:
    pip install PyMuPDF requests
    python download_papers.py              # download PDFs + extract images
    python download_papers.py --move-only  # move PDFs from ~/Downloads, then extract images

Mode 1 (default): Downloads PDFs directly from URLs and extracts images.
Mode 2 (--move-only): After using batch_download.html in Chrome, run this to
    move the downloaded <key>.pdf files from ~/Downloads into each folder,
    then extract images. Useful when direct downloads are blocked.

This script:
1. Reads publications.bib in the same directory
2. Creates a folder for each entry (if not already present)
3. Writes individual .bib files into each folder
4. Downloads (or moves) the PDF
5. Extracts at least 2 images (embedded figures or page renders)

Run from the directory containing publications.bib.
"""

import os
import re
import sys
import time
import shutil
import glob
import requests

try:
    import fitz  # PyMuPDF
except ImportError:
    print("ERROR: PyMuPDF not installed. Run: pip install PyMuPDF")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BIB_PATH = os.path.join(SCRIPT_DIR, "publications.bib")
BASE_DIR = SCRIPT_DIR  # folders created next to publications.bib

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# Seconds to wait between downloads (be polite to servers)
DOWNLOAD_DELAY = 1.0
TIMEOUT = 45  # seconds per request

# ---------------------------------------------------------------------------
# BibTeX parsing
# ---------------------------------------------------------------------------

def parse_bib_entries(bib_text):
    """Split a .bib file into individual entries."""
    entries = []
    raw_entries = re.split(r"\n(?=@)", bib_text.strip())
    for raw in raw_entries:
        raw = raw.strip()
        if not raw:
            continue
        key_match = re.match(r"@\w+\{([^,]+),", raw)
        if not key_match:
            continue
        key = key_match.group(1).strip()
        url_match = re.search(r"url\s*=\s*\{([^}]+)\}", raw)
        url = url_match.group(1).strip() if url_match else None
        entries.append({"key": key, "raw": raw, "url": url})
    return entries

# ---------------------------------------------------------------------------
# URL → PDF URL conversion
# ---------------------------------------------------------------------------

def url_to_pdf_url(url):
    """Convert a landing-page URL to a direct PDF download URL."""
    if not url:
        return None

    # --- ArXiv ---
    if "arxiv.org/abs/" in url:
        return url.replace("/abs/", "/pdf/") + ".pdf"

    # --- OpenReview ---
    if "openreview.net/forum" in url:
        return url.replace("/forum?", "/pdf?")

    # --- NeurIPS proceedings ---
    if "proceedings.neurips.cc" in url and "-Abstract" in url:
        return (
            url.replace("-Abstract-Conference.html", "-Paper-Conference.pdf")
               .replace("-Abstract.html", "-Paper.pdf")
        )

    # --- PMLR (ICML, AISTATS, …) ---
    if "proceedings.mlr.press" in url and url.endswith(".html"):
        base = url.rsplit(".html", 1)[0]
        slug = base.rsplit("/", 1)[1]
        return f"{base}/{slug}.pdf"

    # --- Already a PDF ---
    if url.endswith(".pdf"):
        return url

    # --- Google Patents ---
    if "patents.google.com/patent/" in url:
        patent_id = url.split("/patent/")[1].split("/")[0]
        return f"https://patentimages.storage.googleapis.com/pdfs/{patent_id}.pdf"

    # --- Edinburgh thesis repository ---
    if "era.ed.ac.uk/handle/" in url:
        # The actual bitstream path may vary; this is a best-effort guess
        handle_id = url.split("/handle/")[1]
        return f"https://era.ed.ac.uk/bitstream/{handle_id}/1/Srivastava2019.pdf"

    # --- Springer (chapter / article) ---
    if "link.springer.com/chapter/" in url:
        doi_part = url.replace("https://link.springer.com/chapter/", "")
        return f"https://link.springer.com/content/pdf/{doi_part}.pdf"
    if "link.springer.com/article/" in url:
        doi_part = url.replace("https://link.springer.com/article/", "")
        return f"https://link.springer.com/content/pdf/{doi_part}.pdf"

    # --- Oxford Academic ---
    if "academic.oup.com" in url:
        # Construct PDF URL from article URL
        return url.rstrip("/") + "?redirectedFrom=PDF"

    # --- ASME ---
    if "asmedigitalcollection.asme.org" in url:
        return None  # typically paywalled

    # --- Semantic Scholar ---
    if "semanticscholar.org" in url:
        return None  # no direct PDF; user may find it manually

    # --- Edinburgh research portal ---
    if "research.ed.ac.uk" in url:
        return None

    return None

# ---------------------------------------------------------------------------
# PDF download
# ---------------------------------------------------------------------------

def download_pdf(pdf_url, save_path, max_retries=2):
    """Download a PDF, return True on success."""
    for attempt in range(max_retries + 1):
        try:
            resp = requests.get(
                pdf_url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True
            )
            if resp.status_code == 200:
                ct = resp.headers.get("Content-Type", "")
                if "pdf" in ct.lower() or resp.content[:5] == b"%PDF-":
                    with open(save_path, "wb") as f:
                        f.write(resp.content)
                    return True
                else:
                    print(f"    ⚠ Not a PDF (Content-Type: {ct})")
                    return False
            elif resp.status_code == 403:
                print(f"    ⚠ 403 Forbidden (may be paywalled)")
                return False
            else:
                print(f"    ⚠ HTTP {resp.status_code}")
                if attempt < max_retries:
                    time.sleep(2)
        except requests.exceptions.RequestException as e:
            print(f"    ⚠ {e}")
            if attempt < max_retries:
                time.sleep(2)
    return False

# ---------------------------------------------------------------------------
# Image extraction
# ---------------------------------------------------------------------------

def extract_images(
    pdf_path: str,
    output_dir: str,
    min_images: int = 2,
    max_images: int = 5,
    min_dim: int = 150,
) -> list[str]:
    """
    Extract images from a PDF.

    Strategy:
    1. Try to pull out embedded raster images (figures, plots).
    2. If fewer than min_images found, render selected pages as PNG.
    """
    extracted = []

    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"    ⚠ Cannot open PDF: {e}")
        return extracted

    # --- Pass 1: embedded images ---
    for page_num in range(len(doc)):
        page = doc[page_num]
        for img_idx, img_info in enumerate(page.get_images(full=True)):
            xref = img_info[0]
            try:
                pix = fitz.Pixmap(doc, xref)
                # Skip tiny images (icons, bullets, logos)
                if pix.width < min_dim or pix.height < min_dim:
                    continue
                # Convert CMYK → RGB if needed
                if pix.n >= 5:
                    pix = fitz.Pixmap(fitz.csRGB, pix)

                fname = f"fig_p{page_num+1}_{img_idx+1}.png"
                fpath = os.path.join(output_dir, fname)
                pix.save(fpath)
                extracted.append(fpath)

                if len(extracted) >= max_images:
                    doc.close()
                    return extracted
            except Exception:
                continue

    # --- Pass 2: page renders (fallback) ---
    if len(extracted) < min_images:
        pages_to_render = [0]  # always include first page
        if len(doc) > 2:
            pages_to_render.append(len(doc) // 3)
        if len(doc) > 5:
            pages_to_render.append(2 * len(doc) // 3)

        for pn in pages_to_render:
            if len(extracted) >= min_images:
                break
            try:
                page = doc[pn]
                mat = fitz.Matrix(2, 2)  # 2× zoom for readability
                pix = page.get_pixmap(matrix=mat)
                fname = f"page_{pn+1}.png"
                fpath = os.path.join(output_dir, fname)
                pix.save(fpath)
                extracted.append(fpath)
            except Exception:
                continue

    doc.close()
    return extracted

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def find_downloads_folder():
    """Find the user's Downloads folder."""
    home = os.path.expanduser("~")
    candidates = [
        os.path.join(home, "Downloads"),
        os.path.join(home, "downloads"),
        os.path.join(home, "Download"),
    ]
    for c in candidates:
        if os.path.isdir(c):
            return c
    return os.path.join(home, "Downloads")  # fallback


def move_pdfs_from_downloads(entries):
    """Move <key>.pdf files from ~/Downloads into the correct folders."""
    dl_dir = find_downloads_folder()
    print(f"Looking for PDFs in: {dl_dir}\n")

    moved = 0
    not_found = []

    for entry in entries:
        key = entry["key"]
        folder = os.path.join(BASE_DIR, key)
        dest = os.path.join(folder, f"{key}.pdf")

        # Already in place?
        if os.path.exists(dest) and os.path.getsize(dest) > 5_000:
            continue

        # Look for the file in Downloads (Chrome may add (1), (2) suffixes)
        candidates = glob.glob(os.path.join(dl_dir, f"{key}*.pdf"))
        # Sort so the exact match comes first
        candidates.sort(key=lambda p: (os.path.basename(p) != f"{key}.pdf", p))

        found = False
        for src in candidates:
            if os.path.getsize(src) > 5_000:
                os.makedirs(folder, exist_ok=True)
                shutil.move(src, dest)
                print(f"  ✓ Moved {os.path.basename(src)} → {key}/{key}.pdf")
                moved += 1
                found = True
                break

        if not found:
            not_found.append(key)

    print(f"\nMoved {moved} PDFs. {len(not_found)} not found in Downloads.")
    if not_found and len(not_found) <= 20:
        print(f"  Missing: {', '.join(not_found[:20])}")
    return not_found


def main():
    move_only = "--move-only" in sys.argv

    if not os.path.exists(BIB_PATH):
        print(f"ERROR: {BIB_PATH} not found.")
        print("Place this script next to publications.bib and run again.")
        sys.exit(1)

    with open(BIB_PATH, "r", encoding="utf-8") as f:
        bib_text = f.read()

    entries = parse_bib_entries(bib_text)
    print(f"Found {len(entries)} entries in publications.bib\n")

    # --- Move-only mode: relocate PDFs from ~/Downloads ---
    if move_only:
        print("=" * 60)
        print("MOVE-ONLY MODE")
        print("Moving PDFs from ~/Downloads into publication folders,")
        print("then extracting images.")
        print("=" * 60 + "\n")
        move_pdfs_from_downloads(entries)
        print()

    stats = {"ok": [], "no_url": [], "dl_fail": [], "few_img": []}

    for i, entry in enumerate(entries, 1):
        key = entry["key"]
        url = entry["url"]
        folder = os.path.join(BASE_DIR, key)
        os.makedirs(folder, exist_ok=True)

        print(f"[{i}/{len(entries)}] {key}")

        # --- Write individual .bib ---
        bib_file = os.path.join(folder, f"{key}.bib")
        with open(bib_file, "w", encoding="utf-8") as f:
            f.write(entry["raw"] + "\n")

        # --- Check if PDF already exists (from move or prior download) ---
        pdf_path = os.path.join(folder, f"{key}.pdf")

        if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 5_000:
            print(f"  ✓ PDF present")
        elif not move_only:
            # --- Try downloading ---
            pdf_url = url_to_pdf_url(url)
            if not pdf_url:
                print(f"  ✗ No PDF URL derivable from: {url}")
                stats["no_url"].append(key)
                continue
            print(f"  ↓ {pdf_url}")
            downloaded = download_pdf(pdf_url, pdf_path)
            time.sleep(DOWNLOAD_DELAY)
            if not downloaded:
                stats["dl_fail"].append(key)
                if os.path.exists(pdf_path):
                    os.remove(pdf_path)
                continue
        else:
            print(f"  ✗ PDF not found")
            stats["dl_fail"].append(key)
            continue

        # --- Extract images (skip if already done) ---
        existing_imgs = [f for f in os.listdir(folder) if f.endswith(".png")]
        if len(existing_imgs) >= 2:
            print(f"  ✓ {len(existing_imgs)} images already present")
            stats["ok"].append(key)
            continue

        images = extract_images(pdf_path, folder)
        n = len(images)
        if n >= 2:
            print(f"  ✓ {n} images extracted")
            stats["ok"].append(key)
        elif n > 0:
            print(f"  ~ Only {n} image(s) extracted")
            stats["few_img"].append(key)
        else:
            print(f"  ✗ No images extracted")
            stats["few_img"].append(key)

    # --- Summary ---
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    total = len(entries)
    print(f"Total entries:                {total}")
    print(f"Complete (PDF + ≥2 images):   {len(stats['ok'])}")
    print(f"No PDF URL available:         {len(stats['no_url'])}")
    print(f"PDF missing / download fail:  {len(stats['dl_fail'])}")
    print(f"Fewer than 2 images:          {len(stats['few_img'])}")

    if stats["no_url"]:
        print(f"\n— No PDF URL: {', '.join(stats['no_url'])}")
    if stats["dl_fail"]:
        print(f"\n— Missing/failed: {', '.join(stats['dl_fail'])}")
    if stats["few_img"]:
        print(f"\n— Few images: {', '.join(stats['few_img'])}")

    print("\nDone!")


if __name__ == "__main__":
    main()
