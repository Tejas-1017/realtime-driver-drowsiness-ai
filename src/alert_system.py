import time

class AlertSystem:
    def __init__(self):
        self.alert_active = False

    def trigger_alarm(self, reason="DROWSINESS DETECTED"):
        self.alert_active = True
        print(f"⚠️ [WARNING ALERT] {reason}! BEEP BEEP BEEP!")

    def clear_alarm(self):
        self.alert_active = False
