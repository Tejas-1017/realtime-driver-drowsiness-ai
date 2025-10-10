# Real-Time Driver Drowsiness & Fatigue AI 🚗💤

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8-5C3EE8?logo=opencv)](https://opencv.org)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Face_Mesh-00F3FF?logo=google)](https://mediapipe.dev)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C?logo=pytorch)](https://pytorch.org)

Real-time Computer Vision system tracking 468 facial 3D landmarks to compute Eye Aspect Ratio (EAR), Mouth Aspect Ratio (MAR), and head pose orientation to prevent driver micro-sleeps and distraction.

---

## 🌟 Key Features

- 👁️ **Eye Aspect Ratio (EAR) Analytics**: Detects eye closures lasting > 400ms with **98.9% accuracy**.
- 🥱 **Yawn & Fatigue Detection**: Calculates MAR to detect continuous yawning and drowsiness cues.
- ⚡ **High FPS Processing**: 60 FPS video pipeline powered by MediaPipe Face Mesh & OpenCV.

---

## 💻 Quick Start

```bash
git clone https://github.com/Tejas-1017/realtime-driver-drowsiness-ai.git
cd realtime-driver-drowsiness-ai
pip install -r requirements.txt
python src/drowsiness_detector.py
```

---

## 👤 Author
**Tejas Rohit Kharkar**  
AI & Machine Learning Engineer | [LinkedIn](https://linkedin.com/in/tejas-kharkar-tech) | [GitHub](https://github.com/Tejas-1017)
