#!/usr/bin/env bash

# Serve frontend
cd /app/frontend/dist && python -m http.server 3000 &
FRONTEND_PID=$!

# Run backend
cd /app && pixi run python backend/main.py &
BACKEND_PID=$!

echo "Production servers running. Press Ctrl+C to stop both."

trap 'kill $BACKEND_PID $FRONTEND_PID; echo "Servers stopped."; exit 0' INT

wait
