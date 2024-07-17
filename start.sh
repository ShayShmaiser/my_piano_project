#!/bin/bash

# Ensure PulseAudio is started
pulseaudio --start

# Execute the original entrypoint script
exec /app/entrypoint.sh
