#!/bin/bash
echo "=================================================="
echo "  1-CLICK SETUP & LAUNCHER: realtime-driver-drowsiness-ai"
echo "=================================================="
echo ""
echo "[1/3] Creating Python Virtual Environment (venv)..."
python3 -m venv venv
source venv/bin/activate

echo "[2/3] Installing Dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
pip install gradio

echo ""
echo "[3/3] Launching Interactive Dashboard..."
python3 dashboard.py
