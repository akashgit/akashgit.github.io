# Skill: Convert Publications to Media-Rich Cards

Convert text-only publication entries in publications.md to media-rich publication cards with images from arXiv.

## Instructions for Claude

When this skill is invoked, follow these steps:

### Step 1: Parse and Plan
1. Read `/Users/akash/cursor-projects/akashgit.github.io/publications.md`
2. Identify all text-only publication entries (markdown list items: `* *Title* (Year)`)
3. If a section name was provided as an argument, filter to only that section
4. Count total papers to process and show to user
5. Ask user to confirm before proceeding

### Step 2: Process Papers in Batches

**IMPORTANT**: Use the Task tool with subagent_type=general-purpose to process papers efficiently.

Process papers in batches of 10-15 papers at a time:

1. **Create batch list**: Group remaining papers into manageable batches
2. **For each batch, use Task tool** to delegate the work:

```
Task tool with prompt:
"Process these 10 publications from publications.md and convert them to publication-card format:

[List of 10 paper titles and years]

For each paper:
1. Search arXiv for the paper using WebSearch
2. Download representative figure from arXiv HTML version
3. Resize to 400px width using sips
4. Save to /Users/akash/cursor-projects/akashgit.github.io/publications/images/[theme]/[slug].png
5. Extract authors, venue, and generate description
6. Return the publication-card.html include statement

If a paper can't be found or has no good image, skip it and note why.
"
```

3. **After each batch completes**:
   - Review the generated include statements
   - Edit publications.md to replace text entries with includes
   - Verify images were downloaded correctly

### Step 2 Alternative: Process Each Paper Individually

If batch processing is not suitable, process each text-only publication entry individually:

1. **Extract metadata** from the line:
   - Title (between `* *` and `*`)
   - Year (in parentheses)
   - Venue (if present before year)

2. **Search for paper on arXiv**:
   - Use WebSearch with query: `"[title]" site:arxiv.org`
   - Extract arXiv ID from result

3. **Download representative figure**:
   - Visit arXiv HTML version: `https://arxiv.org/html/[arxiv-id]`
   - If HTML not available, check PDF
   - Identify best figure (Figure 1, Figure 2, overview diagram, architecture)
   - Download image using Bash (curl/wget)
   - Resize to 400px width using sips: `sips -Z 400 input.png --out output.png`
   - Save to appropriate theme directory (see Section Mappings below)
   - Filename format: `[paper-slug].png` (lowercase, hyphens)

4. **Generate paper metadata**:
   - Authors: Extract from arXiv page (highlight Akash Srivastava with `<strong>` tags)
   - Description: Generate 1-sentence summary from abstract (focus on contribution)
   - Links: Paper URL (arXiv required), code URL (if GitHub link found), project URL (if available)
   - BibTeX ID: `firstauthor{year}{keyword}` format (e.g., `srivastava2017veegan`)

5. **Convert to publication-card include**:
   - Replace the text line with publication-card.html include
   - Fill in all parameters (image, title, authors, venue, year, description, paper_url, code_url, project_url, bibtex_id)
   - Preserve the entry's position in the file
   - Maintain proper indentation

6. **Handle errors gracefully**:
   - If paper not found on arXiv: skip and log to progress file
   - If no good image available: skip and log (leave as text-only)
   - If download fails: retry once, then skip and log
   - Continue to next paper (don't stop entire process)

### Step 3: Finalize
1. Rebuild CSS: `npm run build:css`
2. Show summary of:
   - Papers successfully converted
   - Papers skipped (with reasons)
   - Total images downloaded
3. Create git commit with all changes
4. Remind user to check localhost:4000/publications/

## Usage

```
/publications-to-cards [section-name]
```

**Examples:**
- `/publications-to-cards` - Process all remaining text-only publications
- `/publications-to-cards "Inference-Time Scaling"` - Process only the Inference-Time Scaling section
- `/publications-to-cards "Alignment"` - Process only the Alignment section

## What This Skill Does

This skill automates the conversion of text-only publication entries to visual publication cards by:

1. **Parsing publications.md** to identify text-only entries (markdown list items starting with `* *Title*`)
2. **Searching arXiv** for each paper using title and year
3. **Downloading representative figures** from arXiv HTML versions or PDFs
4. **Optimizing images** to 400px width for 2x retina display
5. **Converting entries** to use the `publication-card.html` include component
6. **Handling errors gracefully** - skipping papers without good images or not found on arXiv

## Input Format

The skill looks for text-only publications in this format:

```markdown
* *Title of Paper* (Year)
* *Title of Paper* (Venue Year)
* *Title of Paper* (Year, Additional Info)
```

## Output Format

Each converted entry becomes:

```markdown
{% include publication-card.html
  image="/publications/images/[theme]/[paper-slug].png"
  title="Full Paper Title"
  authors="Author 1, <strong>Akash Srivastava</strong>, Author 3"
  venue="Venue Name"
  year="2024"
  description="One-sentence description of the paper"
  paper_url="https://arxiv.org/abs/..."
  code_url="https://github.com/..."
  bibtex_id="firstauthor2024keyword"
%}
```

## Directory Structure

Images are saved to theme-specific directories:

```
/publications/images/
  ├── alignment/
  ├── diffusion/
  ├── generative/
  ├── inference-scaling/
  ├── representation-learning/
  ├── structured-models/
  ├── causal/
  ├── neural-processes/
  └── variational-inference/
```

## Processing Strategy

### Paper Priority (if processing all)

1. **High Priority** - Recent papers (2024-2025) with strong visual content
2. **Medium Priority** - 2020-2023 papers with good diagrams
3. **Low Priority** - Older papers and workshop papers

### Image Selection Criteria

For each paper, the skill tries to find:
1. **Overview/method diagram** - Shows the approach at a high level
2. **Architecture diagram** - Shows the model structure
3. **Key results visualization** - Shows main experimental findings
4. **Figure 1 or Figure 2** - Usually the most representative

### Fallback Behavior

If no suitable image is found:
- **Option 1**: Leave as text-only entry (recommended)
- **Option 2**: Use generic theme icon (if you create them)
- **Option 3**: Extract first page of PDF as image

## Section Mappings

The skill maps publication sections to image directories:

| Section Name | Image Directory |
|--------------|----------------|
| Inference-Time Scaling, Sampling, & Probabilistic Inference | inference-scaling |
| Alignment, Preference Learning, & Human Feedback | alignment |
| Model Merging, Fine-Tuning, & Parameter Efficiency | generative |
| Diffusion Models & Generative Modeling | diffusion |
| Synthetic Data, Privacy, & Density Ratio Estimation | generative |
| Red-Teaming, Robustness, & Evaluation | generative |
| Foundation Models for Planning, Design, & Systems | generative |
| Lifelong Learning, Program Synthesis, & Modularity | generative |
| Core Generative Modeling & Bayesian ML | generative |
| Applied / Cross-Domain Modeling | generative |
| Representation Learning & Neural Processes | representation-learning |
| Structured & Compositional Models | structured-models |
| Causal Inference & Counterfactuals | causal |

**Directory Creation**: If a directory doesn't exist, create it:
```bash
mkdir -p /Users/akash/cursor-projects/akashgit.github.io/publications/images/[theme]
```

## Configuration

### Papers to Skip

The skill automatically skips:
- Papers already converted to publication-card format
- Papers marked with `[no-image]` tag
- PhD thesis entries
- Survey papers (unless marked for inclusion)

### Papers to Prioritize

Papers with these markers get processed first:
- `[priority]` - Process this paper first
- `[has-project]` - Paper has project page (likely has images)
- `[landmark]` - Important foundational work

## Example: Adding Markers

```markdown
## Alignment, Preference Learning, & Human Feedback

* *Dr. SoW: Density Ratio of Strong-over-Weak LLMs* (2024) [priority]
* *Houdini: Lifelong Learning as Program Synthesis* (2018) [landmark] [has-project]
* *Some Workshop Paper* (2020) [no-image]
```

## Implementation Details

The skill uses:
1. **WebSearch** - To find arXiv links for papers
2. **WebFetch** - To download arXiv HTML pages
3. **Bash** - To download and optimize images using curl/wget and imagemagick/sips
4. **Read/Write/Edit** - To modify publications.md
5. **Grep/Glob** - To parse and navigate the file

## Success Criteria

A successful conversion includes:
- ✅ Image downloaded and optimized (400px width)
- ✅ Image saved to correct theme directory
- ✅ Publication entry converted to use include
- ✅ All metadata filled in (title, authors, venue, year, description)
- ✅ Links added (paper URL minimum, code/project if available)
- ✅ BibTeX ID generated in format: `firstauthor{year}{keyword}`

## Progress Tracking

The skill creates a progress file at `.claude/publications-conversion-progress.json` with:
- Papers processed
- Papers skipped (with reasons)
- Papers failed (with error messages)
- Images downloaded
- Total progress percentage

## Error Handling

If a paper fails to process:
1. Log the error to progress file
2. Continue to next paper (don't stop entire process)
3. At the end, show summary of successes and failures

## Post-Processing

After conversion, the skill:
1. Rebuilds CSS with `npm run build:css`
2. Shows summary of changes
3. Offers to commit changes to git
4. Displays preview URL (localhost:4000/publications/)

## Example Templates

### Input (Text-Only Entry)

```markdown
* *Curiosity-Driven Red-Teaming for Large Language Models* (2024)
```

### Output (Media-Rich Card)

```markdown
{% include publication-card.html
  image="/publications/images/generative/curiosity-red-teaming.png"
  title="Curiosity-Driven Red-Teaming for Large Language Models"
  authors="Zhang Zhang, Liyao Xiang, Diyi Yang, Srini Iyer, <strong>Akash Srivastava</strong>"
  venue="arXiv preprint"
  year="2024"
  description="A curiosity-driven approach to automatically discover diverse failure modes in LLMs by generating novel test cases that maximize model uncertainty."
  paper_url="https://arxiv.org/abs/2402.xxxxx"
  bibtex_id="zhang2024curiosity"
%}
```

### Full Example with All Links

```markdown
{% include publication-card.html
  image="/publications/images/generative/compositional-planning.png"
  title="Compositional Foundation Models for Hierarchical Planning"
  authors="Anurag Ajay, Seungwook Han, Yilun Du, Shuang Li, <strong>Akash Srivastava</strong>, et al."
  venue="NeurIPS"
  year="2023"
  description="Hierarchical planning framework combining task, visual, and action planning using foundation models with feedback mechanisms for long-horizon robotic tasks."
  paper_url="https://arxiv.org/abs/2309.08587"
  project_url="https://hierarchical-planning-foundation-model.github.io/"
  code_url="https://github.com/anuragajay/hip"
  bibtex_id="ajay2023compositional"
%}
```

### Text-Only Fallback (No Image Found)

If no suitable image is found, leave as text-only:

```markdown
* *Some Paper Without Good Figures* (2020)
```

## Quick Reference: Image Download Commands

```bash
# Download from arXiv HTML
curl -o /tmp/figure.png "https://arxiv.org/html/[arxiv-id]/[figure-filename]"

# Resize to 400px width
sips -Z 400 /tmp/figure.png --out /Users/akash/cursor-projects/akashgit.github.io/publications/images/[theme]/[slug].png

# Check image size
sips -g pixelWidth -g pixelHeight /path/to/image.png
```

## Notes

- The skill preserves the original order of publications
- Text-only entries can remain alongside media-rich cards
- You can run the skill multiple times (it skips already-converted entries)
- The skill is incremental - you can convert one section at a time
- Always highlight "Akash Srivastava" in authors with `<strong>` tags
- Use "et al." if more than 5 authors
- Prefer arXiv links over other sources for "paper_url"
- Only include code_url if official GitHub repo exists (not forks)
- Project URLs should be live demonstration/documentation sites
