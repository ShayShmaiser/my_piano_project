# FROM python:3.8-slim

# ENV PYTHONUNBUFFERED=1
# ENV SDL_AUDIODRIVER=dummy
# ENV SDL_VIDEODRIVER=x11
# ENV DISPLAY=:99


# RUN apt-get update && \
#     python -m pip install --upgrade pip && \
#     apt-get install -y python3-dev xvfb \
#     libsdl2-dev \
#     libsdl2-image-dev \
#     libsdl2-mixer-dev \
#     libsdl2-ttf-dev \
#     libsmpeg-dev \
#     libportmidi-dev \
#     libavformat-dev \
#     libswscale-dev \
#     libjpeg-dev \
#     libfreetype6-dev \
#     alsa-utils \
#     alsa-oss \
#     libasound2 \
#     procps && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# # RUN pip install numpy PyOpenGL pygame pygame-ce pygame_gui

# WORKDIR /app

# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . /app/

# COPY __init__.py /usr/local/lib/python3.8/site-packages/pygame/__init__.py
# COPY ui_tab_container.py /usr/local/lib/python3.8/site-packages/pygame_gui/elements/ui_tab_container.py
# COPY gui_font_pygame.py /usr/local/lib/python3.8/site-packages/pygame_gui/core/gui_font_pygame.py


# COPY entrypoint.sh /app/entrypoint.sh
# RUN chmod +x /app/entrypoint.sh


# # CMD ["python3", "main.py"]
# ENTRYPOINT ["/app/entrypoint.sh"]










# #################################
# FROM python:3.8-slim

# ENV MONGO_URL="mongodb://shayshmaiser:PmRtpwEnX6CldTMb@mongodb-service:27017/bikorotDB"
# # ENV SDL_AUDIODRIVER="dummy"
# ENV SDL_VIDEODRIVER="x11"
# ENV DISPLAY=":99"

# ENV PYTHONUNBUFFERED=1
# ENV SDL_AUDIODRIVER=alsa
# # ENV SDL_VIDEODRIVER=x11
# # ENV DISPLAY=:0
# # ENV PULSE_SERVER=unix:/run/user/1000/pulse/native
# RUN apt-get update && \
#     apt-get install -y wget tar curl xvfb x11vnc
# RUN apt-get update && \
#     apt-get install -y \
#         alsa-utils \
#         pulseaudio \
#         dbus-x11 \
#         x11vnc \
#         xvfb \
#         x11-apps \
#         python3-dev \
#         libsdl2-dev \
#         libsdl2-image-dev \
#         libsdl2-mixer-dev \
#         libsdl2-ttf-dev \
#         libsmpeg-dev \
#         libportmidi-dev \
#         libavformat-dev \
#         libswscale-dev \
#         libjpeg-dev \
#         libfreetype6-dev \
#         alsa-oss \
#         libasound2 \
#         procps \
#         libx11-dev \
#         libxext-dev \
#         libxcb1-dev \
#         libx11-xcb-dev \
#         libxcb-keysyms1-dev \
#         libxcb-randr0-dev \
#         libxcb-render-util0-dev \
#         libxcb-render0-dev \
#         libxcb-shape0-dev \
#         libxcb-shm0-dev \
#         libxcb-xfixes0-dev \
#         libxcb-sync-dev \
#         libxcb-image0-dev \
#         libxcb-icccm4-dev \
#         libxcb-xinerama0-dev \
#         libxcb-xkb-dev \
#         libxcb-util-dev \
#         libxkbcommon-x11-dev \
#         libxkbcommon-dev && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*
# RUN pip install numpy PyOpenGL pygame pygame-ce pygame_gui
# RUN pip install pymongo pygame

# RUN echo "pcm.!default null" > /root/.asoundrc && \
#     echo "ctl.!default null" >> /root/.asoundrc

# RUN mkdir -p /app/pulse /var/run/pulse /var/cache/pulse
# COPY pulseaudio.default.pa /etc/pulse/default.pa
# RUN echo "default-server = unix:/run/user/1000/pulse/native" > /etc/pulse/client.conf

# RUN echo "defaults.pcm.card 0" > /etc/asound.conf && \
#     echo "defaults.ctl.card 0" >> /etc/asound.conf

# WORKDIR /app

# # COPY pulse-client.conf /etc/pulse/client.conf
# # COPY asound.conf /etc/asound.conf

# RUN mkdir -p /var/run/pulse /var/cache/pulse
# RUN echo "default-server = unix:/run/user/1000/pulse/native" > /etc/pulse/client.conf

# ENV PULSE_SERVER /var/run/pulse/native
# ENV PULSE_COOKIE /var/run/pulse/cookie

# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . /app/

# COPY pulseaudio.default.pa /etc/pulse/default.pa

# COPY __init__.py /usr/local/lib/python3.8/site-packages/pygame/__init__.py
# COPY ui_tab_container.py /usr/local/lib/python3.8/site-packages/pygame_gui/elements/ui_tab_container.py
# COPY gui_font_pygame.py /usr/local/lib/python3.8/site-packages/pygame_gui/core/gui_font_pygame.py
# COPY cookie /app/cookie

# COPY start.sh /app/start.sh
# RUN chmod +x /app/start.sh

# COPY pulseaudio.default.pa /etc/pulse/default.pa
# # CMD ["pulseaudio", "--start", "--exit-idle-time=-1", "--daemonize"]

# COPY entrypoint.sh /app/entrypoint.sh
# RUN chmod +x /app/entrypoint.sh
# CMD ["pulseaudio", "--start"]
# # CMD ["/app/start.sh"]
# # CMD ["/app/entrypoint.sh"]
# # CMD ["python3", "main.py"]
# # ENTRYPOINT ["/app/entrypoint.sh"]
# # ENTRYPOINT ["/app/entrypoint.sh"]
# ENTRYPOINT ["sh", "-c", "Xvfb :99 -screen 0 1280x720x24 & python3 main.py"]





# FROM python:3.8-slim

# ENV PYTHONUNBUFFERED=1
# ENV SDL_AUDIODRIVER=pulse
# ENV SDL_VIDEODRIVER=x11
# ENV DISPLAY=:99
# # ENV SDL_AUDIODRIVER=dummy
# # ENV SDL_VIDEODRIVER=x11
# # ENV DISPLAY=:99
# RUN apt-get update && \
#     apt-get install -y pulseaudio x11vnc xvfb x11-apps python3-dev \
#                        libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev \
#                        libsdl2-ttf-dev libsmpeg-dev libportmidi-dev \
#                        libavformat-dev libswscale-dev libjpeg-dev \
#                        libfreetype6-dev alsa-utils alsa-oss libasound2 procps && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*
# RUN apt-get update && apt-get install -y \
#     x11vnc \
#     xvfb \
#     x11-apps

# RUN apt-get update && \
#     python -m pip install --upgrade pip && \
#     apt-get install -y python3-dev xvfb \
#     libsdl2-2.0-0 \
#     libsdl2-dev \
#     libsdl2-mixer-2.0-0 \
#     libsdl2-image-dev \
#     libsdl2-mixer-dev \
#     libsdl2-ttf-dev \
#     libsmpeg-dev \
#     libportmidi-dev \
#     libavformat-dev \
#     libswscale-dev \
#     libjpeg-dev \
#     libfreetype6-dev \
#     alsa-utils \
#     alsa-oss \
#     libasound2 \
#     procps && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# # RUN pip install numpy PyOpenGL pygame pygame-ce pygame_gui
# RUN python -m pip install --upgrade pip && \
#     pip install pygame

# COPY pulseaudio-default.pa /etc/pulse/default.pa
# RUN echo 'exit-idle-time = -1' > /etc/pulse/daemon.conf && \
#     echo 'load-module module-native-protocol-unix auth-anonymous=1 socket=/tmp/pulse-native' >> /etc/pulse/default.pa

# RUN mkdir -p /app /app/pulse

# RUN mkdir -p /app/pulse_native
# RUN chmod -R 777 /app/pulse_native

# RUN mkdir -p /app /app/pulse /app/pulse_native
# RUN chmod -R 777 /app/pulse_native

# COPY entrypoint.sh /app/entrypoint.sh
# RUN chmod +x /app/entrypoint.sh


# WORKDIR /app

# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . /app/


# COPY __init__.py /usr/local/lib/python3.8/site-packages/pygame/__init__.py
# COPY ui_tab_container.py /usr/local/lib/python3.8/site-packages/pygame_gui/elements/ui_tab_container.py
# COPY gui_font_pygame.py /usr/local/lib/python3.8/site-packages/pygame_gui/core/gui_font_pygame.py
# COPY cookie /app/cookie

# COPY start.sh /app/start.sh
# RUN chmod +x /app/start.sh





# # CMD ["/app/start.sh"]
# # CMD ["/app/entrypoint.sh"]
# # CMD ["python3", "main.py"]
# # ENTRYPOINT ["/app/entrypoint.sh"]
# # CMD pulseaudio --start --system=false --disallow-module-loading=no --exit-idle-time=-1 & /app/entrypoint.sh
# ENTRYPOINT ["/app/entrypoint.sh"]
# CMD ["python3", "main.py"]






FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1
ENV SDL_AUDIODRIVER=dummy  
ENV SDL_VIDEODRIVER=x11
ENV DISPLAY=:99

RUN apt-get update && \
    apt-get install -y x11vnc xvfb x11-apps python3-dev \
                       libsdl2-dev libsdl2-image-dev \
                       libsdl2-ttf-dev libsmpeg-dev \
                       libportmidi-dev libavformat-dev \
                       libswscale-dev libjpeg-dev \
                       libfreetype6-dev procps && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip

RUN mkdir -p /app

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

COPY __init__.py /usr/local/lib/python3.8/site-packages/pygame/__init__.py
COPY ui_tab_container.py /usr/local/lib/python3.8/site-packages/pygame_gui/elements/ui_tab_container.py
COPY gui_font_pygame.py /usr/local/lib/python3.8/site-packages/pygame_gui/core/gui_font_pygame.py

COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Set VNC password
RUN mkdir -p /root/.vnc \
    && x11vnc -storepasswd yourpassword /root/.vnc/passwd

CMD ["/app/entrypoint.sh"]







# ENV SDL_AUDIODRIVER=pulse
# ENV SDL_VIDEODRIVER=x11
# ENV DISPLAY=:99

# RUN apt-get update && \
#     apt-get install -y pulseaudio x11vnc xvfb x11-apps python3-dev \
#                        libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev \
#                        libsdl2-ttf-dev libsmpeg-dev libportmidi-dev \
#                        libavformat-dev libswscale-dev libjpeg-dev \
#                        libfreetype6-dev alsa-utils alsa-oss libasound2 procps && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# # Ensure pip is updated and pygame is installed
# RUN python -m pip install --upgrade pip && \
#     pip install pygame

# Create directories and set permissions as root
# RUN mkdir -p /app /app/pulse /app/pulse_native /tmp/.X11-unix && \
#     chmod -R 1777 /tmp/.X11-unix && \
#     chmod -R 777 /app/pulse_native

# # Copy entrypoint script and make it executable
# COPY entrypoint.sh /app/entrypoint.sh
# RUN chmod +x /app/entrypoint.sh

# # Create user and set up home directory
# RUN useradd -ms /bin/bash myuser && \
#     mkdir -p /home/myuser/.config/pulse && \
#     chown -R myuser:myuser /home/myuser

# Prepare PulseAudio configuration before switching to user
# COPY pulseaudio-default.pa /home/myuser/.config/pulse/default.pa
# COPY daemon.conf /home/myuser/.config/pulse/daemon.conf
# RUN chown -R myuser:myuser /home/myuser/.config

# # Switch to user
# USER myuser

# # Set the working directory and copy application files
# WORKDIR /app
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# Copy additional required files
# COPY . /app/
# COPY __init__.py /usr/local/lib/python3.8/site-packages/pygame/__init__.py
# COPY ui_tab_container.py /usr/local/lib/python3.8/site-packages/pygame_gui/elements/ui_tab_container.py
# COPY gui_font_pygame.py /usr/local/lib/python3.8/site-packages/pygame_gui/core/gui_font_pygame.py
# COPY cookie /app/cookie

# Start the application using the entrypoint script
# ENTRYPOINT ["/app/entrypoint.sh"]
# CMD ["python3", "main.py"]