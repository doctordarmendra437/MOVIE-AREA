FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y ffmpeg wget

# Upgrade pip
RUN pip install --upgrade pip setuptools wheel

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Run your bot
CMD ["python3", "bot.py"]
