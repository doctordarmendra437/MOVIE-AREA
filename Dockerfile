# Use official lightweight Python image
FROM python:3.10-slim

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies (needed for tgcrypto, ffmpeg, etc.)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    gcc \
    libssl-dev \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Upgrade pip + install deps
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port (Render expects this)
EXPOSE 8080

# Start command (update if your entrypoint is different)
CMD ["python", "bot.py"]
