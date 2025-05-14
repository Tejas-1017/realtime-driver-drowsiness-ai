import numpy as np

class LandmarkExtractor:
    # Key landmark indices for 468 3D MediaPipe Mesh
    LEFT_EYE = [362, 385, 387, 263, 373, 380]
    RIGHT_EYE = [33, 160, 158, 133, 153, 144]
    MOUTH = [61, 291, 0, 17, 84, 314]

    @staticmethod
    def calculate_ear(eye_landmarks):
        # Compute vertical Euclidean distances
        v1 = np.linalg.norm(eye_landmarks[1] - eye_landmarks[5])
        v2 = np.linalg.norm(eye_landmarks[2] - eye_landmarks[4])
        # Compute horizontal distance
        h = np.linalg.norm(eye_landmarks[0] - eye_landmarks[3])
        ear = (v1 + v2) / (2.0 * h)
        return ear

    @staticmethod
    def calculate_mar(mouth_landmarks):
        v = np.linalg.norm(mouth_landmarks[2] - mouth_landmarks[3])
        h = np.linalg.norm(mouth_landmarks[0] - mouth_landmarks[1])
        return v / h if h > 0 else 0
