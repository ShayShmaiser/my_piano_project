FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1
ENV SDL_AUDIODRIVER=dummy
ENV SDL_VIDEODRIVER=x11
ENV DISPLAY=:99


RUN apt-get update && \
    python -m pip install --upgrade pip && \
    apt-get install -y python3-dev xvfb \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libsmpeg-dev \
    libportmidi-dev \
    libavformat-dev \
    libswscale-dev \
    libjpeg-dev \
    libfreetype6-dev \
    alsa-utils \
    alsa-oss \
    libasound2 \
    procps && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# RUN pip install numpy PyOpenGL pygame pygame-ce pygame_gui

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

COPY __init__.py /usr/local/lib/python3.8/site-packages/pygame/__init__.py
COPY ui_tab_container.py /usr/local/lib/python3.8/site-packages/pygame_gui/elements/ui_tab_container.py
COPY gui_font_pygame.py /usr/local/lib/python3.8/site-packages/pygame_gui/core/gui_font_pygame.py


COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh


# CMD ["python3", "main.py"]
ENTRYPOINT ["/app/entrypoint.sh"]