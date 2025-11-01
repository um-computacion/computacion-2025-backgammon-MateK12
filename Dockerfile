FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libfreetype6-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV SDL_VIDEODRIVER=dummy
ENV SDL_AUDIODRIVER=dummy
ENV SDL_HIDDEN=1
ENV PYTHONUNBUFFERED=1

RUN useradd -m backgammon && chown -R backgammon:backgammon /app
USER backgammon

EXPOSE 8000

CMD ["python", "-m", "pytest", "-v", "--cov=src", "--cov-report=html"]