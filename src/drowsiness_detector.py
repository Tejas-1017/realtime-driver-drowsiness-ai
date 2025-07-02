import cv2
import numpy as np
from src.landmark_extractor import LandmarkExtractor
from src.alert_system import AlertSystem

class DriverDrowsinessDetector:
    def __init__(self, ear_thresh=0.22, consec_frames=20):
        self.ear_thresh = ear_thresh
        self.consec_frames = consec_frames
        self.frame_counter = 0
        self.alert = AlertSystem()

    def process_frame(self, frame):
        # Simulated EAR calculation
        mock_ear = 0.25 # Nominal open eye
        
        # Overlay HUD metrics
        cv2.putText(frame, f"EAR: {mock_ear:.2f}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, "DRIVER STATUS: ALERT", (30, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        return frame

if __name__ == "__main__":
    detector = DriverDrowsinessDetector()
    print("Driver Drowsiness AI initialized successfully.")
