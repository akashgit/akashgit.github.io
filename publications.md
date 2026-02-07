---
layout: default
title: Publications - Akash Srivastava
---

# Publications

A comprehensive list of publications organized by research theme.

**Primary Research Areas:** `Inference-Time Scaling`, `Agent Evaluation`, `LLM Alignment`, `Probabilistic Inference`, `Generative Models`

**Secondary Research Areas:** `Diffusion Models`, `Synthetic Data`, `Continual Learning`, `Enterprise AI Systems`

---

## Inference-Time Scaling, Sampling, & Probabilistic Inference (LLMs)

**Tags:** `inference-time-scaling`, `particle-methods`, `monte-carlo`, `llms`, `sampling`, `bayesian-inference`

* *Mitigating Premature Exploitation in Particle-based Monte Carlo for Inference-Time Scaling* (2025)
* *Rollout Roulette: A Probabilistic Inference Approach to Inference-Time Scaling of LLMs* (2025)
* *A Probabilistic Inference Approach to Inference-Time Scaling of LLMs Using Particle-Based Monte Carlo Methods* (2025)
* *Inference-Time Scaling of Diffusion Language Models with Particle Gibbs Sampling* (2025)
* *Variational Russian Roulette for Deep Bayesian Nonparametrics* (2019)

---

## Alignment, Preference Learning, & Human Feedback

**Tags:** `alignment`, `preference-learning`, `rlhf`, `density-ratios`, `human-feedback`

{% include publication-card.html
  image="/publications/images/alignment/lab-method.png"
  title="LAB: Large-Scale Alignment for chatBots"
  authors="Guanlin Li, Yifei Yuan, Baharan Mirzasoleiman, <strong>Akash Srivastava</strong>"
  venue="arXiv preprint"
  year="2024"
  description="A taxonomy-driven approach to synthetic data generation for LLM alignment, enabling chatbots to handle diverse real-world queries through multi-phase training."
  paper_url="https://arxiv.org/abs/2403.01081"
  bibtex_id="li2024lab"
%}

* *Dr. SoW: Density Ratio of Strong-over-Weak LLMs for Reducing the Cost of Human Annotation* (2024)
* *Preference Data Annotation with Guided Density Ratios*
* *Value-Augmented Sampling for Language Model Alignment and Personalization* (2024)
* *Post-Processing Differentially Private Synthetic Data* (2025)

---

## Model Merging, Fine-Tuning, & Parameter Efficiency

**Tags:** `fine-tuning`, `model-merging`, `parameter-efficiency`, `continual-learning`

* *Activation-Informed Merging of Large Language Models* (2025)
* *Sculpting Subspaces: Constrained Full Fine-Tuning in LLMs for Continual Learning* (2025)
* *Squat: Subspace-Orthogonal KV Cache Quantization* (2025)
* *Unveiling the Secret Recipe: A Guide for Supervised Fine-Tuning Small LLMs* (2024)

---

## Diffusion Models & Generative Modeling

**Tags:** `diffusion-models`, `generative-models`, `optimization`, `constraints`

{% include publication-card.html
  image="/publications/images/diffusion/soda.png"
  title="SODA: Spectral Orthogonal Decomposition Adaptation for Diffusion Models"
  authors="Jiancheng Huang, <strong>Akash Srivastava</strong>, et al."
  venue="arXiv preprint"
  year="2025"
  description="Parameter-efficient fine-tuning for diffusion models using spectral orthogonal decomposition, outperforming LoRA and other PEFT methods."
  paper_url="https://arxiv.org/abs/2405.21050"
  bibtex_id="huang2025soda"
%}

{% include publication-card.html
  image="/publications/images/diffusion/dice.png"
  title="DICE: Discrete Inversion Enabling Controllable Editing for Multinomial Diffusion and Masked Generative Models"
  authors="Xiaoxiao He, Ligong Han, <strong>Akash Srivastava</strong>, et al."
  venue="arXiv preprint"
  year="2024"
  description="A novel discrete inversion method enabling controllable editing in multinomial diffusion models without relying on continuous ODE approximations."
  paper_url="https://arxiv.org/abs/2410.08207"
  bibtex_id="he2024dice"
%}

* *Aligning Optimization Trajectories with Diffusion Models for Constrained Design Generation* (2023)
* *Spectrum-Aware Parameter-Efficient Fine-Tuning for Diffusion Models* (2024)

---

## Synthetic Data, Privacy, & Density Ratio Estimation

**Tags:** `synthetic-data`, `privacy`, `density-ratio-estimation`, `dp`

* *Differentially Private Synthetic Data Generation for Relational Databases* (2024)
* *Private Synthetic Data Meets Ensemble Learning* (2023)
* *Scaling Densities for Improved Density Ratio Estimation*
* *Estimating the Density Ratio Between Distributions with High Discrepancy* (2023)

---

## Red-Teaming, Robustness, & Evaluation

**Tags:** `robustness`, `red-teaming`, `evaluation`, `failure-modes`

* *Curiosity-Driven Red-Teaming for Large Language Models* (2024)
* *On the Importance of Calibration in Semi-Supervised Learning* (2022)
* *Mitigating Confirmation Bias in Semi-Supervised Learning* (2023)

---

## Foundation Models for Planning, Design, & Systems

**Tags:** `foundation-models`, `planning`, `design`, `optimization`

{% include publication-card.html
  image="/publications/images/generative/compositional-planning.png"
  title="Compositional Foundation Models for Hierarchical Planning"
  authors="Anurag Ajay, Seungwook Han, Yilun Du, Shuang Li, <strong>Akash Srivastava</strong>, et al."
  venue="NeurIPS"
  year="2023"
  description="Hierarchical planning framework combining task, visual, and action planning using foundation models with feedback mechanisms for long-horizon robotic tasks."
  paper_url="https://arxiv.org/abs/2309.08587"
  project_url="https://hierarchical-planning-foundation-model.github.io/"
  bibtex_id="ajay2023compositional"
%}

* *Learning Joint Representations of Design and Performance Spaces* (2024)
* *Beyond Statistical Similarity: Rethinking Metrics for Deep Generative Models in Engineering Design* (2023)

---

## Lifelong Learning, Program Synthesis, & Modularity

**Tags:** `lifelong-learning`, `program-synthesis`, `modularity`

* *Houdini: Lifelong Learning as Program Synthesis* (2018)
* *A Probabilistic Framework for Modular Continual Learning* (2023)
* *Synthesis of Differentiable Functional Programs for Lifelong Learning* (2018)

---

## Core Generative Modeling & Bayesian ML (Foundational Work)

**Tags:** `variational-inference`, `bayesian-ml`, `generative-models`

{% include publication-card.html
  image="/publications/images/generative/veegan.png"
  title="VEEGAN: Reducing Mode Collapse in GANs using Implicit Variational Learning"
  authors="<strong>Akash Srivastava</strong>, Lazar Valkov, Chris Russell, Michael U. Gutmann, Charles Sutton"
  venue="NeurIPS"
  year="2017"
  description="A principled approach to reducing mode collapse in GANs by adding a reconstructor network that ensures the generator is approximately invertible."
  paper_url="https://arxiv.org/abs/1705.07761"
  code_url="https://github.com/akashgit/VEEGAN"
  bibtex_id="srivastava2017veegan"
%}

{% include publication-card.html
  image="/publications/images/variational-inference/avitm.png"
  title="Autoencoding Variational Inference For Topic Models"
  authors="<strong>Akash Srivastava</strong>, Charles Sutton"
  venue="ICLR"
  year="2017"
  description="Black-box variational inference framework for topic models using neural networks to learn flexible inference distributions."
  paper_url="https://arxiv.org/abs/1703.01488"
  code_url="https://github.com/akashgit/autoencoding_vi_for_topic_models"
  bibtex_id="srivastava2017autoencoding"
%}

* *Fast and Scalable Bayesian Deep Learning by Weight-Perturbation in Adam* (ICML 2018)
* *Deep Generative Modelling for Amortised Variational Inference* (PhD Thesis)

---

## Applied / Cross-Domain Modeling

**Tags:** `urban-systems`, `logistics`, `transportation`

* *Learning to Deliver: A Foundation Model for Vehicle Routing* (2024)
* *Urban Context and Delivery Performance* (2024)

---

*For complete citation information and PDFs, please visit my [Google Scholar profile](https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en).*
