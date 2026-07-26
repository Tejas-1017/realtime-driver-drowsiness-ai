@echo off
echo ==================================================
echo   1-CLICK SETUP & LAUNCHER: realtime-driver-drowsiness-ai
echo ==================================================
echo.
echo [1/3] Creating Python Virtual Environment (venv)...
python -m venv venv
call venv\Scripts\activate

echo [2/3] Installing Dependencies...
pip install --upgrade pip
pip install -r requirements.txt
pip install gradio

echo.
echo [3/3] Launching Interactive Dashboard...
python dashboard.py
pause
