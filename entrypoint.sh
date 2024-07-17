#!/bin/bash
# Start X virtual framebuffer
Xvfb :99 -screen 0 1024x768x16 &

# Start PulseAudio
pulseaudio --start --file=/home/myuser/.config/pulse/default.pa --disallow-exit --disallow-module-loading --exit-idle-time=-1 --no-cpu-limit --disable-shm=true --system=false

# Delay to ensure services start
sleep 5

# Launch the main Python application
exec python3 main.py





# if [ "$USE_XVFB" = "true" ]; then
#     echo "Starting Xvfb..."
#     Xvfb :99 -screen 0 1280x1024x24 &
#     export DISPLAY=:99
#     echo "Xvfb started with PID $!"
# else
#     echo "Using external X server..."
# fi

# echo "DISPLAY is set to $DISPLAY"
# echo "Running the Python application..."
# 