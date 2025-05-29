FROM python:3.10

# Entwicklerwerkzeuge installieren
RUN apt-get update && apt-get install -y \
    git \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Arbeitsverzeichnis anlegen
WORKDIR /workspace

# Python-Tools
RUN pip install --upgrade pip
RUN pip install pytest flask
