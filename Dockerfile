FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run both bot and web server
CMD ["sh", "-c", "python bot.py & python web.py"]
