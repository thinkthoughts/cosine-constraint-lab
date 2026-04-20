# 🔬 Cosine Constraint Lab

**Measure the angle between construction and collapse.**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/00_angle_theory.ipynb)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

## 🎯 Core Thesis

> **The 45° angle is the universal critical threshold where Valid Construction (VC) collapses into Invalid Assignment (IA).**

| Angle | Status | Interpretation |
|-------|--------|----------------|
| **θ < 10°** | **VC / GOS** | Valid Construction — signal dominates, stable |
| **θ ≈ 45°** | **IA / ZOS** | Invalid Assignment — collapse, inconsistency |
| **θ > 55°** | **Broken** | Noise dominates, unreliable |

This principle appears across mathematics, machine learning, AI alignment, physics, economics, psychology, engineering, and network science.

## 📚 Notebook Series (00 → 09)

| Notebook | Title | Focus | Colab |
|:--------:|-------|-------|:-----:|
| **00** | Angle Theory | Geometric foundation of the 45° constraint | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/00_angle_theory.ipynb) |
| **01** | Cosine Constraint Basics | Core functions | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/01_cosine_constraint_basics.ipynb) |
| **02** | Math Claims Hydration | PCSP dichotomy, mathematical claims | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/02_math_claims_hydration.ipynb) |
| **03** | Equation Consistency | IA vs VC equation systems | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/03_equation_consistency.ipynb) |
| **04** | ML Embedding Alignment | Signal vs noise, detecting embedding drift | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/04_ml_embedding_alignment.ipynb) |
| **05** | Agent Consistency Check | Belief-action alignment in AI agents | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/05_agent_consistency_check.ipynb) |
| **06** | Phase Lock Demo | Interactive 45° boundary explorer | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/06_phase_lock_demo.ipynb) |
| **07** | Triplet Progression Simulation | Dynamic phase evolution over time | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/07_triplet_progression_simulation.ipynb) |
| **08** | Real-World Case Studies | LLM hallucination, paper review, model drift | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/08_real_world_case_studies.ipynb) |
| **09** | Cross-Domain Synthesis | Physics, economics, psychology, engineering, networks | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/09_cross_domain_synthesis.ipynb) |

## 🚀 Quick Start

### Option 1: Run in Colab (Recommended — No Installation)
Click any Colab badge above to open a notebook instantly.

### Option 2: Run Locally

```bash
git clone https://github.com/thinkthoughts/cosine-constraint-lab.git
cd cosine-constraint-lab
pip install -r requirements.txt
jupyter notebook notebooks/00_angle_theory.ipynb
```

### Option 3: Try the Interactive Demo First

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/notebooks/06_phase_lock_demo.ipynb)

**Notebook 06** is the most interactive — drag the slider and watch the 45° collapse in real time.

## 🔗 Connection to `triplet-phase-lock`

This lab is the computational companion to [`triplet-phase-lock`](https://github.com/thinkthoughts/triplet-phase-lock):

| `triplet-phase-lock` | `cosine-constraint-lab` |
|----------------------|--------------------------|
| Π⁽⁰⁾ expand | Notebook 00 (angle theory) |
| Π⁽¹⁾ extend | Notebooks 01-02 (basics + math) |
| Π⁽²⁾ resist | Notebooks 03-05 (equations + ML + agents) |
| Π⁽³⁾ synthesis | Notebooks 06-09 (demo + simulation + cases + synthesis) |
| IA/ZOS (45° collapse) | Measured and visualized across all notebooks |
| VC/GOS (locked <10°) | Verified through constraint-preserving construction |

## 📊 Core Visualization

```
Stability
   1.0 |████████████                                   
       |████████████                                   
   0.8 |████████████                                   
       |████████████                                   
   0.7 |────────────┐  ← 45° CRITICAL POINT (cos=0.707)
       |            │                                   
   0.5 |            │                                   
       |            │                                   
   0.3 |            │                                   
       |            │                                   
   0.0 └────────────┴────────────────────────────►
       0°   10°    45°    55°           90°
       │           │                    │
       │           │                    │
    VC Lock     COLLAPSE              Broken
    (Stable)    (IA/ZOS)           (Noise)
```

## 🧪 What You Can Test

| Domain | Question | Notebook |
|--------|----------|----------|
| **Mathematics** | Is this PCSP claim hydrated or dry? | 02 |
| **Equations** | Does `2 = 0.96` collapse? (Yes — at 45°) | 03 |
| **ML Embeddings** | Has my model drifted off-manifold? | 04 |
| **AI Agents** | Do actions follow stated beliefs? | 05 |
| **Your Own Claim** | Rate it on 5 constraints → get angle | 06, 08 |
| **Physics** | Where is the phase transition? | 09 |
| **Economics** | Is the market approaching a bubble? | 09 |

## 📁 Repository Structure

```
cosine-constraint-lab/
├── notebooks/
│   ├── 00_angle_theory.ipynb
│   ├── 01_cosine_constraint_basics.ipynb
│   ├── 02_math_claims_hydration.ipynb
│   ├── 03_equation_consistency.ipynb
│   ├── 04_ml_embedding_alignment.ipynb
│   ├── 05_agent_consistency_check.ipynb
│   ├── 06_phase_lock_demo.ipynb
│   ├── 07_triplet_progression_simulation.ipynb
│   ├── 08_real_world_case_studies.ipynb
│   └── 09_cross_domain_synthesis.ipynb
├── src/
│   └── cosine_lock.py
├── requirements.txt
├── LICENSE
└── README.md
```

## 🔧 Requirements

```txt
numpy>=1.21.0
matplotlib>=3.4.0
ipywidgets>=7.6.0
scikit-learn>=1.0.0
sympy>=1.9
```

## 📖 Learning Path

| Step | Notebook | Time | What You Learn |
|:----:|----------|:----:|----------------|
| 1 | 00 | 5 min | The 45° cosine constraint geometrically |
| 2 | 01 | 10 min | Core functions |
| 3 | 02 | 15 min | Test PCSP claims (your seminar) |
| 4 | 03 | 10 min | IA vs VC equation systems |
| 5 | 04 | 15 min | Detect embedding drift |
| 6 | 05 | 15 min | Monitor agent consistency |
| 7 | 06 | 10 min | Interactive 45° exploration |
| 8 | 07 | 15 min | Dynamic phase simulation |
| 9 | 08 | 20 min | Real-world case studies |
| 10 | 09 | 15 min | Cross-domain synthesis |

**Total: ~2 hours** to complete the entire lab.

## 🎓 Connection to PCSP Research

In your seminar on *Promise Constraint Satisfaction Problems (PCSPs)*:

| Claim | Angle | Status | Why |
|-------|-------|--------|-----|
| *"Some dichotomy results for Mal'cev algebras; general case open"* | **<10°** | **VC/GOS** | Hydrated — respects all constraints |
| *"The PCSP dichotomy is true for all finite algebras"* | **≈45°** | **IA/ZOS** | Dry — collapses without construction |

The speaker's actual claim is **VC**. The over-extrapolated claim is **IA** — exactly the 45° collapse point.

## 🤝 Related Work

- [`triplet-phase-lock`](https://github.com/thinkthoughts/triplet-phase-lock) — Structural foundation (IA vs VC, ZOS vs GOS)
- [`constraint-labs`](https://github.com/thinkthoughts/constraint-labs) — Filtering and stability
- [`quantum-systems`](https://github.com/thinkthoughts/quantum-systems) — Physical instantiations
- [`agent-systems`](https://github.com/thinkthoughts/agent-systems) — Executable constraints

## 📝 License

MIT License — see [LICENSE](LICENSE) file.

## 🙏 Acknowledgments

Inspired by the `triplet-phase-lock` framework and the open problem of PCSP dichotomy for finite algebras.

---

**Stay locked below 10°. At 45°, collapse is inevitable.** 🔒

```python
# The core principle
construction != assignment
constraint -> signal > noise
angle < 10° -> VC/GOS (stable)
angle ≈ 45° -> IA/ZOS (collapse)
```
