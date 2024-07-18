#!/bin/bash

# Start X virtual framebuffer in the background
Xvfb :99 -screen 0 1280x720x16 &

# Start x11vnc server with password and optimized settings
x11vnc -usepw -forever -display :99 -noxdamage &

# Start the Pygame application
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