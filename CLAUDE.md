# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based GitHub Pages personal academic website hosted at akashgit.github.io. The site showcases research work, publications, news, and blog posts for a machine learning researcher.

## Technology Stack

- **Static Site Generator**: Jekyll (GitHub Pages compatible)
- **Markdown Processor**: Kramdown with MathJax math engine
- **Math Rendering**: KaTeX (client-side)
- **Analytics**: Google Analytics (UA-87695573-1)
- **Comments**: Disqus (for blog posts)
- **Styling**: Custom CSS (`/css/main.css`)

## Site Structure

```
/
├── _layouts/          # Jekyll templates
│   ├── default.html   # Main layout with nav, footer, KaTeX, analytics
│   └── post.html      # Blog post layout (extends default, adds comments)
├── _posts/            # Blog posts (YYYY-MM-DD-title.md format)
├── blog/              # Blog index
├── css/               # Stylesheets
├── research/          # Research project pages and PDFs
├── media/             # Media content
├── simgan/            # SimGAN project with traversals subdirectories
├── swim/              # SWIM project
├── Neural-Variational-Inference/  # Approximate inference content
├── config.yml         # Jekyll configuration
└── index.md           # Homepage (main landing page)
```

## Configuration

The site is configured via `config.yml`:
- Site owner: Akash Srivastava
- Blog permalinks: `/blog/:year/:month/:day/:title`
- Math engine: MathJax via Kramdown

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

The site supports both inline and display math equations:
- Inline: `<script type='math/tex'>equation</script>`
- Display: `<script type='math/tex; mode=display'>equation</script>`
- KaTeX renders these client-side via JavaScript in `default.html`

## Local Development

This is a standard Jekyll/GitHub Pages site. To run locally:

```bash
# Install Jekyll and dependencies (if not already installed)
gem install jekyll bundler

# Serve the site locally
jekyll serve

# Site will be available at http://localhost:4000
```

## Deployment

This site uses GitHub Pages, so deployment is automatic:
- Push to `master` branch
- GitHub Pages automatically builds and deploys the Jekyll site
- No manual build/deployment commands needed

## Key Layout Features

The `default.html` layout includes:
- Navigation with links to Home, Google Scholar, CV, LinkedIn, Twitter
- Google Analytics tracking
- KaTeX math rendering setup
- Disqus comments integration (conditional, based on page front matter)
- Footer with contact links
