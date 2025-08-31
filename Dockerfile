# Use official Python base image
FROM python:3.10-slim

# Prevent interactive prompts during apt install
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies (ffmpeg + wget + gcc for some Python libs)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    wget \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run your app (adjust if different)
CMD ["python", "bot.py"]
