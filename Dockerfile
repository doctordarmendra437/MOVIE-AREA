FROM python:3.10-slim

WORKDIR /app

# Install dependencies required for numpy, opencv, pillow, ffmpeg, etc.
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    git \
    ffmpeg \
    libsm6 \
    libxext6 \
    libgl1 \
    python3-dev \
    libssl-dev \
    libffi-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot code
COPY . .

# Run bot (change bot.py to your file)
CMD ["python", "bot.py"]
