# 🧬 BioFrontiers Computational Biology Labs

This directory contains hydration analyses of research labs from the [BioFrontiers Institute's Computational Biology program](https://www.colorado.edu/biofrontiers/computational-biology) at CU Boulder.

Each analysis applies the **45° principle** from the Cosine Constraint Lab to evaluate whether a lab's research program is **VC (Valid Construction)** or **IA (Invalid Assignment)** — measuring how well-articulated, specific, and impactful the lab's mission and methods are.

---

## 📊 Quick Summary

| Metric | Value |
|--------|-------|
| **Total labs analyzed** | 17 |
| **Average hydration** | 94.6% |
| **Average angle** | ~5.5° |
| **VC/GOS labs** | 16/17 |
| **Highest hydration** | Spencer Lab (99%) |

---

## 📁 Directory Structure

```
labs/
├── index.ipynb              # Master index with all analyses and rankings
├── alistar/
│   └── analysis.ipynb
├── allen/
│   └── analysis.ipynb
├── chuong/
│   └── analysis.ipynb
├── clauset/
│   └── analysis.ipynb
├── donaldson/
│   └── analysis.ipynb
├── dowell/
│   └── analysis.ipynb
├── kissler/
│   └── analysis.ipynb
├── krauter/
│   └── analysis.ipynb
├── larremore/
│   └── analysis.ipynb
├── layer/
│   └── analysis.ipynb
├── mukherjee/
│   └── analysis.ipynb
├── myers/
│   └── analysis.ipynb
├── olm/
│   └── analysis.ipynb
├── peleg/
│   └── analysis.ipynb
├── rinn/
│   └── analysis.ipynb
├── spencer/
│   └── analysis.ipynb
└── sprenger/
    └── analysis.ipynb
```

---

## 🏆 Lab Rankings

| Rank | Lab | PI | Hydration | Verdict |
|------|-----|-----|-----------|---------|
| 1 | **Spencer** | Sabrina Spencer | 99% | ✅ VC |
| 2 | **Larremore** | Daniel Larremore | 98% | ✅ VC |
| 3 | **Peleg** | Orit Peleg | 98% | ✅ VC |
| 4 | **Rinn** | John Rinn | 98% | ✅ VC |
| 5 | **Clauset** | Aaron Clauset | 97% | ✅ VC |
| 6 | **Kissler** | Stephen Kissler | 97% | ✅ VC |
| 7 | **Myers** | Chris Myers | 97% | ✅ VC |
| 8 | **Mukherjee** | Debanjan Mukherjee | 96% | ✅ VC |
| 9 | **Donaldson** | Zoe Donaldson | 96% | ✅ VC |
| 10 | **Dowell** | Robin Dowell | 96% | ✅ VC |
| 11 | **Chuong** | Ed Chuong | 92% | ✅ VC |
| 12 | **Layer** | Ryan Layer | 91% | ✅ VC |
| 13 | **Olm** | Matthew Olm | 91% | ✅ VC |
| 14 | **Sprenger** | Kayla Sprenger | 90% | ✅ VC |
| 15 | **Krauter** | Kenneth Krauter | 90% | ✅ VC |
| 16 | **Alistar** | Alistar Lab | 91% | ✅ VC |
| 17 | **Allen** | Mary Ann Allen | 86% | ⚠️ weak VC |

---

## 🔬 What Each Analysis Contains

Each `analysis.ipynb` includes:

| Section | Description |
|---------|-------------|
| **Mission Statement** | The lab's stated research goals |
| **Core Research Areas** | Key focus areas and questions |
| **Key Methods** | Technologies and approaches used |
| **Key Discoveries/Publications** | Notable research outputs |
| **Constraint Dimensions** | 8-10 dimensions scored 0-1 |
| **Angle & Hydration Score** | Quantitative VC/IA measurement |
| **Triplet Phase Mapping** | Π⁽⁰⁾ → Π⁽³⁾ progression |
| **Peer Review Summary** | Evaluation of the research program |
| **Comparison** | How the lab compares to others |

---

## 📈 Key Patterns Across Labs

| Pattern | High Hydration Labs | Lower Hydration Labs |
|---------|---------------------|----------------------|
| **Specific methods** | ✅ Spencer (fluorescent sensors), Larremore (network science) | ⚠️ Allen ("computational programs") |
| **Clear problem statement** | ✅ All top labs | ⚠️ Allen (vague) |
| **Awards & recognition** | ✅ Spencer (all major awards), Larremore (Waterman) | — |
| **Distinctive niche** | ✅ Peleg (fireflies), Donaldson (prairie voles), Rinn (lncRNA) | ⚠️ Allen (crowded field) |
| **Translational impact** | ✅ Larremore (WHO), Spencer (Cancer Moonshot) | — |

---

## 🚀 How to Run These Notebooks

### Option 1: Run in Colab

Click the badge below to open the index notebook in Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/labs/index.ipynb)

### Option 2: Run Locally

```bash
cd cosine-constraint-lab
pip install -r ../requirements.txt
jupyter notebook labs/index.ipynb
```

---

## 📖 How to Interpret the Scores

| Hydration | Angle | Verdict | Meaning |
|-----------|-------|---------|---------|
| >90% | <10° | ✅ VC / GOS | Well-constructed, specific, impactful |
| 80-90% | 10-20° | ⚠️ weak VC | Needs more specificity or measurable outcomes |
| <80% | >20° | ❌ IA / ZOS | Vague claims, likely over-hyped |

---

## 🔗 Connection to Cosine Constraint Lab

These lab analyses apply the framework from the main [Cosine Constraint Lab](../README.md):

| Lab Notebook | Applied in Lab Analysis |
|--------------|------------------------|
| 00_angle_theory | Geometric foundation |
| 01_cosine_constraint_basics | Core functions (angle, lock_status) |
| 02_math_claims_hydration | Constraint dimensions for research claims |
| 06_phase_lock_demo | Interactive angle visualization |
| 07_triplet_progression_simulation | Phase mapping for research programs |
| 08_real_world_case_studies | Peer review format |

---

## 📝 How to Add a New Lab Analysis

1. **Create a new directory** in `labs/`:
   ```bash
   mkdir labs/[lab_name]
   ```

2. **Copy the template** from an existing analysis (e.g., `alistar/analysis.ipynb`)

3. **Fill in the lab's information**:
   - Mission statement
   - Core research areas
   - Key methods
   - Key discoveries/publications
   - Score each constraint dimension (0-1)

4. **Calculate angle and hydration** using the provided functions

5. **Update `index.ipynb`** with the new lab's metrics

6. **Commit and push** to the repository

---

## 🙏 Acknowledgments

These analyses are based on publicly available information from the [BioFrontiers Institute](https://www.colorado.edu/biofrontiers/) and individual lab websites. They are intended as educational examples of applying the cosine constraint framework to evaluate research programs.

---

**Stay locked below 10°. At 45°, research programs collapse into irrelevance.** 🔒
