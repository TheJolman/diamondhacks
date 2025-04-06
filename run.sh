#!/usr/bin/env bash

cd frontend || exit
npm run build

cd .. || exit
pixi run python3 backend/main.py
