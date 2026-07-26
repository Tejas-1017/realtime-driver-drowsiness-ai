from fastapi import FastAPI
app = FastAPI(title="Driver Drowsiness Monitoring API")

@app.get("/")
def root():
    return {"status": "ACTIVE", "system": "Driver Drowsiness AI"}

@app.get("/telemetry")
def telemetry():
    return {"ear": 0.28, "mar": 0.12, "perclos": "3.4%", "driver_status": "FOCUSED"}
