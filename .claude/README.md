# Claude Skills for akashgit.github.io

This directory contains custom skills for working with the Jekyll-based academic website.

## Available Skills

### `/publications-to-cards`

Converts text-only publication entries to media-rich publication cards with images from arXiv.

**What it does:**
- Parses publications.md to find text-only entries (markdown lists)
- Searches arXiv for each paper
- Downloads and optimizes representative figures
- Converts entries to use the publication-card.html component
- Generates complete metadata (authors, description, links)

**Usage:**
```bash
# Process all remaining text-only publications
/publications-to-cards

# Process only a specific section
/publications-to-cards "Inference-Time Scaling"
/publications-to-cards "Alignment"
/publications-to-cards "Diffusion Models"
```

**Example transformation:**

Before (text-only):
```markdown
* *Curiosity-Driven Red-Teaming for Large Language Models* (2024)
```

After (media-rich card):
```markdown
{% include publication-card.html
  image="/publications/images/generative/curiosity-red-teaming.png"
  title="Curiosity-Driven Red-Teaming for Large Language Models"
  authors="Zhang Zhang, Liyao Xiang, <strong>Akash Srivastava</strong>"
  venue="arXiv preprint"
  year="2024"
  description="Curiosity-driven approach to discover diverse LLM failure modes."
  paper_url="https://arxiv.org/abs/2402.xxxxx"
%}
```

**Current Status:**
- ✅ Infrastructure in place (component, CSS, JavaScript)
- ✅ 6 papers already converted with images:
  - LAB: Large-Scale Alignment for chatBots (2024)
  - SODA: Spectral Orthogonal Decomposition Adaptation (2025)
  - DICE: Discrete Inversion for Multinomial Diffusion (2024)
  - Compositional Foundation Models for Hierarchical Planning (2023)
  - VEEGAN (NeurIPS 2017)
  - Autoencoding Variational Inference For Topic Models (ICLR 2017)
- 📝 ~74 papers remaining to convert

**See:** `.claude/skills/publications-to-cards.md` for detailed documentation

## How Skills Work

Skills are markdown files in `.claude/skills/` that provide instructions to Claude Code.

When you invoke a skill with `/skill-name`, Claude reads the skill file and follows the instructions to complete the task.

## Creating New Skills

To create a new skill:

1. Create a markdown file in `.claude/skills/`
2. Include "Instructions for Claude" section with clear step-by-step instructions
3. Add usage examples and documentation
4. Test the skill by invoking it with `/skill-name`

## Skill Best Practices

- **Be explicit**: Provide exact file paths, command formats, and expected outputs
- **Include examples**: Show input/output transformations
- **Handle errors**: Specify what to do when things fail
- **Use Task tool**: For complex multi-step operations, use Task tool with subagent
- **Track progress**: Create progress files for long-running operations
- **Commit changes**: Always create git commits after successful operations

## Notes

- Skills are project-specific and live in this repository
- Skills can invoke other Claude Code tools (Bash, Read, Write, Edit, Task, etc.)
- Skills persist across sessions - you can invoke them anytime
- Skills can accept arguments (e.g., section names, file paths)
