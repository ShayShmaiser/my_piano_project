#!/bin/bash

echo "Starting Xvfb..."
Xvfb :99 -screen 0 1280x720x16 &
XVFB_PID=$!
export DISPLAY=:99

echo "Xvfb started with PID $XVFB_PID"
echo "Running the Python application..."

python3 main.py

# Keep the container running to view logs if the application exits
wait $XVFB_PID