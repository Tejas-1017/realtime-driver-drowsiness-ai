import cv2
import numpy as np
import time

class DrowsinessDetector:
    def __init__(self, ear_threshold=0.21, consecutive_frames=20):
        self.ear_threshold = ear_threshold
        self.consecutive_frames = consecutive_frames
        self.drowsy_counter = 0
        self.alarm_active = False

    def calculate_ear(self, eye_landmarks):
        # Calculate Eye Aspect Ratio (EAR) distance formula
        A = np.linalg.norm(eye_landmarks[1] - eye_landmarks[5])
        B = np.linalg.norm(eye_landmarks[2] - eye_landmarks[4])
        C = np.linalg.norm(eye_landmarks[0] - eye_landmarks[3])
        ear = (A + B) / (2.0 * C + 1e-6)
        return ear

    def process_frame(self, frame):
        h, w, _ = frame.shape

        # Simulated landmarks
        simulated_ear = 0.26 + 0.05 * np.sin(time.time() * 2)

        if simulated_ear < self.ear_threshold:
            self.drowsy_counter += 1
            if self.drowsy_counter >= self.consecutive_frames:
                self.alarm_active = True
        else:
            self.drowsy_counter = 0
            self.alarm_active = False

        status_str = "DROWSINESS ALARM ACTIVE!" if self.alarm_active else "DRIVER ALERT & FOCUSED"
        color = (0, 0, 255) if self.alarm_active else (0, 255, 0)

        cv2.putText(frame, f"EAR: {simulated_ear:.2f} | {status_str}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        return frame, self.alarm_active

if __name__ == '__main__':
    detector = DrowsinessDetector()
    dummy_frame = np.zeros((480, 640, 3), dtype=np.uint8)
    out_frame, alarm = detector.process_frame(dummy_frame)
    print(f"[DROWSINESS AI] Engine Active. Initial EAR Alert State: {alarm}")
