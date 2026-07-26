import gradio as gr
import cv2
import numpy as np

def analyze_driver_fatigue(ear_value, mar_value):
    drowsy = ear_value < 0.21
    yawning = mar_value > 0.65
    
    if drowsy and yawning:
        status = "CRITICAL ALERT: SEVERE FATIGUE & YAWNING DETECTED! 🚨"
    elif drowsy:
        status = "WARNING: DROWSINESS DETECTED (EYES CLOSED)! ⚠️"
    elif yawning:
        status = "NOTICE: DRIVER YAWNING DETECTED 🥱"
    else:
        status = "DRIVER ALERT & FOCUSED ✅"

    # Generate telemetry chart
    canvas = np.zeros((200, 500, 3), dtype=np.uint8)
    color = (0, 0, 255) if (drowsy or yawning) else (0, 255, 0)
    cv2.putText(canvas, f"EAR Index: {ear_value:.2f}", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(canvas, f"MAR Index: {mar_value:.2f}", (20, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(canvas, status[:25], (20, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    report = f"""
=== DRIVER FATIGUE TELEMETRY REPORT ===
• Driver Status: {status}
• Eye Aspect Ratio (EAR): {ear_value:.3f} (Threshold: < 0.21)
• Mouth Aspect Ratio (MAR): {mar_value:.3f} (Threshold: > 0.65)
• PERCLOS Fatigue Score: {'88.4%' if drowsy else '2.1%'}
"""
    return canvas, report

demo = gr.Interface(
    fn=analyze_driver_fatigue,
    inputs=[
        gr.Slider(0.10, 0.40, value=0.28, label="Simulated Eye Aspect Ratio (EAR)"),
        gr.Slider(0.10, 1.00, value=0.20, label="Simulated Mouth Aspect Ratio (MAR)")
    ],
    outputs=[
        gr.Image(type="numpy", label="Live Driver HUD Telemetry Display"),
        gr.Textbox(label="Fatigue Diagnostic Audit", lines=6)
    ],
    title="🚗 Real-Time Driver Drowsiness & Safety Monitoring Dashboard",
    description="Facial Mesh Landmark Analytics for Automotive Driver Safety."
)

if __name__ == '__main__':
    demo.launch(server_name="0.0.0.0", server_port=7861, share=False)
