import numpy as np

def compute_ear(eye_points):
    """
    Computes Eye Aspect Ratio (EAR) using 6 eye facial landmark coordinates.
    Formula: EAR = (||p2-p6|| + ||p3-p5||) / (2 * ||p1-p4||)
    """
    p1, p2, p3, p4, p5, p6 = eye_points
    v1 = np.linalg.norm(p2 - p6)
    v2 = np.linalg.norm(p3 - p5)
    h = np.linalg.norm(p1 - p4)
    if h == 0:
        return 0.0
    return (v1 + v2) / (2.0 * h)

def compute_mar(mouth_points):
    """
    Computes Mouth Aspect Ratio (MAR) for yawn detection.
    """
    p1, p2, p3, p4, p5, p6 = mouth_points
    v1 = np.linalg.norm(p2 - p6)
    v2 = np.linalg.norm(p3 - p5)
    h = np.linalg.norm(p1 - p4)
    if h == 0:
        return 0.0
    return (v1 + v2) / (2.0 * h)
