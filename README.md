# 🔬 Cosine Constraint Lab

**Measure the angle between construction and collapse.**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/00_angle_theory.ipynb)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

## 🎯 Core Thesis

> **The 45° angle is the universal critical threshold where Valid Construction (VC) collapses into Invalid Assignment (IA).**

At **θ < 10°** → **VC / GOS** — Valid Construction, signal dominates, stable  
At **θ ≈ 45°** → **IA / ZOS** — Invalid Assignment, collapse, inconsistency  
At **θ > 55°** → **Broken** — Noise dominates, unreliable

This principle appears across mathematics, machine learning, AI alignment, physics, economics, psychology, engineering, and network science.

## 📚 Notebook Series (00 → 09)

| Notebook | Title | Focus | Colab |
|:--------:|-------|-------|:-----:|
| **00** | Angle Theory | Geometric foundation of the 45° constraint | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/00_angle_theory.ipynb) |
| **01** | Cosine Constraint Basics | Core functions: `angle_degrees()`, `lock_status()` | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/01_cosine_constraint_basics.ipynb) |
| **02** | Math Claims Hydration | PCSP dichotomy, mathematical claims (your seminar) | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/02_math_claims_hydration.ipynb) |
| **03** | Equation Consistency | IA vs VC equation systems (`2 = 0.96` vs `√-1.96 = 1.4i`) | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/03_equation_consistency.ipynb) |
| **04** | ML Embedding Alignment | Signal vs noise, detecting embedding drift | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/04_ml_embedding_alignment.ipynb) |
| **05** | Agent Consistency Check | Belief-action alignment in AI agents | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/05_agent_consistency_check.ipynb) |
| **06** | Phase Lock Demo | Interactive 45° boundary explorer | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/06_phase_lock_demo.ipynb) |
| **07** | Triplet Progression Simulation | Dynamic phase evolution over time | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/07_triplet_progression_simulation.ipynb) |
| **08** | Real-World Case Studies | LLM hallucination, paper review, model drift | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/08_real_world_case_studies.ipynb) |
| **09** | Cross-Domain Synthesis | Physics, economics, psychology, engineering, networks | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/09_cross_domain_synthesis.ipynb) |

## 🚀 Quick Start (2 minutes)

### Option 1: Run in Colab (Recommended)

Click any Colab badge above to open a notebook instantly — no installation required.

### Option 2: Run Locally

```bash
git clone https://github.com/thinkthoughts/cosine-constraint-lab.git
cd cosine-constraint-lab
pip install -r requirements.txt
jupyter notebook notebooks/00_angle_theory.ipynb
