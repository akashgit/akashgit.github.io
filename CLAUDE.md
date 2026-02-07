# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## ⚠️ IMPORTANT: Local Development Environment Check (EVERY SESSION)

**At the start of EVERY new session, you MUST:**

1. Check if the local development server is running at http://localhost:4000
2. If NOT running, ask the user to start it before proceeding with any work

**To start the local development environment:**

```bash
# Option 1: Using npm script (recommended)
npm run serve

# Option 2: Using bundle directly
bundle exec jekyll serve

# The site will be available at http://localhost:4000
```

**Why this matters:**
- Changes to layouts and CSS are auto-rebuilt by Jekyll
- The user can see changes in real-time at localhost:4000
- Testing is immediate without deploying to production
- Ruby 3.2.0 and bundler are already installed and configured

**How to check:**
```bash
curl -s http://localhost:4000 | head -1
# Should return: <!DOCTYPE html>
```

If the dev server isn't running, provide the startup command and wait for confirmation before proceeding.

---

## Project Overview

This is a Jekyll-based GitHub Pages personal academic website hosted at akashgit.github.io. The site showcases research work, publications, news, and blog posts for a machine learning researcher.

## Technology Stack

- **Static Site Generator**: Jekyll (GitHub Pages compatible)
- **Build Tool**: npm for Tailwind CSS compilation
- **Styling**: Tailwind CSS 3.x with Typography plugin
- **Markdown Processor**: Kramdown with MathJax math engine
- **Math Rendering**: KaTeX 0.16.11 (client-side, vanilla JavaScript)
- **Analytics**: Removed (was Google Analytics UA, which stopped working July 2024)
- **Comments**: Disqus (for blog posts)
- **Ruby Version**: 3.2.0 (configured locally)

## Site Structure

```
/
├── _layouts/          # Jekyll templates
│   ├── default.html   # Main layout with responsive nav, footer, KaTeX
│   └── post.html      # Blog post layout (extends default, adds comments)
├── _posts/            # Blog posts (YYYY-MM-DD-title.md format)
├── blog/              # Blog index
├── css/
│   ├── input.css      # Tailwind source file
│   └── main.css       # Generated CSS (do not edit directly)
├── research/          # Research project pages and PDFs
├── media/             # Media content
├── simgan/            # SimGAN project with traversals subdirectories
├── swim/              # SWIM project
├── Neural-Variational-Inference/  # Approximate inference content
├── _config.yml        # Jekyll configuration
├── tailwind.config.js # Tailwind CSS configuration
├── postcss.config.js  # PostCSS configuration
├── package.json       # npm scripts
└── index.md           # Homepage (main landing page)
```

## Configuration

The site is configured via `_config.yml`:
- Site owner: Akash Srivastava
- Blog permalinks: `/blog/:year/:month/:day/:title`
- Math engine: MathJax via Kramdown (outputs `\(...\)` and `\[...\]` notation)
- Markdown: GFM (GitHub Flavored Markdown)

## Content Guidelines

### Blog Posts

- Place in `_posts/` directory
- Filename format: `YYYY-MM-DD-title.md`
- Front matter required:
  ```yaml
  ---
  layout: post
  title: "Post Title"
  date: YYYY-MM-DD
  ---
  ```
- Posts automatically get Disqus comments via `post.html` layout

### Pages

- Use front matter:
  ```yaml
  ---
  layout: default
  title: Page Title
  ---
  ```
- Homepage (`index.md`) contains news, current projects, and professional bio

### Math Support

The site supports both inline and display math equations using Kramdown notation:
- **Inline math**: `$$equation$$` or `\(equation\)`
  - Kramdown outputs: `\(equation\)`
- **Display math**: `\[equation\]`
  - Kramdown outputs: `\[equation\]`
- KaTeX 0.16.11 renders these client-side via vanilla JavaScript in `default.html`
- Math rendering script handles both Kramdown's `\(...\)` notation and legacy `<script type='math/tex'>` tags

## Local Development

### Prerequisites
- Ruby 3.2.0 (already installed)
- Bundler (already configured)
- Node.js and npm (for Tailwind CSS)

### Starting the Development Server

```bash
# Build CSS and start Jekyll server (watches for changes)
npm run serve

# Or separately:
npm run build:css          # Build Tailwind CSS once
npm run watch:css          # Watch and rebuild CSS on changes
bundle exec jekyll serve   # Start Jekyll server
```

The site will be available at **http://localhost:4000**

### Making CSS Changes

When editing `css/input.css`, you need to rebuild:
```bash
npm run build:css
```

Or use watch mode during development:
```bash
npm run watch:css
```

Jekyll auto-rebuilds HTML/Markdown changes, but CSS requires the Tailwind build step.

## Deployment

This site uses GitHub Pages, so deployment is automatic:
- Push to `master` branch
- GitHub Pages automatically builds and deploys the Jekyll site
- No manual build/deployment commands needed
- **Important**: Commit `css/main.css` (the generated file) along with `css/input.css`

## Layout Features

### `default.html` Layout

Modern responsive layout with:
- **Responsive Navigation**:
  - Desktop (≥768px): Horizontal navigation bar
  - Mobile (<768px): Hamburger menu with slide-down navigation
- **Semantic HTML5**: `<header>`, `<main>`, `<footer>`, proper ARIA labels
- **KaTeX Math Rendering**: Vanilla JavaScript (no jQuery)
- **Tailwind Styling**: Utility-first CSS with Typography plugin
- **Disqus Comments**: Conditional loading based on page front matter
- **No Analytics**: Google Analytics removed (UA deprecated July 2024)

### `post.html` Layout

Extends `default.html` with:
- Semantic `<article>` and `<time>` tags
- Blog post styling via Tailwind Typography
- Automatic comment section (Disqus)

## Important Notes for Claude

1. **Always check localhost:4000 is running** at session start
2. **Never edit `css/main.css` directly** - it's auto-generated from `css/input.css`
3. **After editing `css/input.css`**, run `npm run build:css`
4. **Ruby environment**: Use Ruby 3.2.0, not system Ruby
5. **Math rendering**: Site uses Kramdown's `\(...\)` notation, rendered by KaTeX client-side
6. **No jQuery**: Site uses vanilla JavaScript only
7. **Responsive breakpoint**: Mobile menu activates at <768px width
8. **Test in browser DevTools**: Use responsive mode to test mobile navigation

## Common Tasks

### Add a new blog post
1. Create `_posts/YYYY-MM-DD-title.md`
2. Add front matter with layout, title, date
3. Write content with Markdown and math notation
4. Jekyll auto-rebuilds when you save

### Update CSS styling
1. Edit `css/input.css`
2. Run `npm run build:css`
3. Check localhost:4000 for changes
4. Commit both `input.css` and `main.css`

### Test responsive design
1. Open http://localhost:4000 in browser
2. Press F12 → Toggle device toolbar (Cmd+Shift+M)
3. Set width <768px to see mobile menu
4. Test hamburger menu toggle

### Test math rendering
1. Visit http://localhost:4000/blog/2017/03/13/unsaturating_softmax
2. Verify equations render correctly
3. Check browser console for KaTeX errors
