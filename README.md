# cosine-constraint-lab

**Measure the angle between construction and collapse.**

This lab implements the core hypothesis from [triplet-phase-lock](https://github.com/thinkthoughts/triplet-phase-lock):

> A claim, equation, or embedding is **consistent** iff its angular distance from its constraint basis is **< 10°** (VC/GOS).  
> At **45°**, it enters the critical zone — maximally unstable, prone to IA/ZOS collapse.

## Quick Start (Colab)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/cosine-constraint-lab/blob/main/colab/run_all.ipynb)

## What You Can Test

- **Math claims**: Is "P = NP" at 0° (anchored) or 45° (assigned)?
- **Equation systems**: Does `2 = 0.96` collapse (IA) or `√-1.96 = 1.4i` hold (VC)?
- **ML embeddings**: Is your semantic drift within the 10° lock?
- **Agent beliefs**: Is the agent's output constrained by its inputs?

## Core Function

```python
from src.cosine_lock import claim_angle

result = claim_angle(claim_vector, constraint_basis)
# → {'status': 'IA / ZOS', 'angle_degrees': 45.0, 'phase': '45° critical zone'}
