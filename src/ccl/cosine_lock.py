import numpy as np
from typing import Union, List, Dict

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Return cos(θ) between two vectors."""
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def angle_degrees(a: np.ndarray, b: np.ndarray) -> float:
    """Return angle in degrees between vectors a and b."""
    cos = cosine_similarity(a, b)
    return np.arccos(np.clip(cos, -1.0, 1.0)) * 180 / np.pi

def lock_status(angle: float) -> Dict[str, Union[str, float]]:
    """Classify angle into VC/IA/ZOS states."""
    if angle < 10:
        return {"status": "VC / GOS", "phase": "locked", "interpretation": "Valid construction — constraint preserved"}
    elif angle < 35:
        return {"status": "weak VC", "phase": "drifting", "interpretation": "Partially constructed — risk of collapse"}
    elif angle <= 55:  # 45° ± 10°
        return {"status": "IA / ZOS", "phase": "45° critical zone", "interpretation": "Invalid assignment — unstable, prone to inconsistency"}
    elif angle < 80:
        return {"status": "weak IA", "phase": "decoupled", "interpretation": "Mostly unconstrained — noise dominant"}
    else:
        return {"status": "orthogonal", "phase": "irrelevant", "interpretation": "No relationship — independent domain"}

def claim_angle(claim_vector: np.ndarray, constraint_basis: np.ndarray) -> Dict:
    """Given a claim and its supposed constraint basis, return the angle and lock status."""
    angle = angle_degrees(claim_vector, constraint_basis)
    status = lock_status(angle)
    status["angle_degrees"] = angle
    return status
