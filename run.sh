#!/usr/bin/env bash

pixi run python3 backend/main.py &
BACKEND_PID=$!

cd frontend && pixi run npm run dev &
FRONTEND_PID=$!

echo "Servers running. Press Ctrl+C to stop both."

trap 'kill $BACKEND_PID $FRONTEND_PID; echo "Servers stopped."; exit 0' INT

wait
