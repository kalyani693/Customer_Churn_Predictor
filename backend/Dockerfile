FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh


COPY . .

EXPOSE 8000
CMD ["./wait-for-it.sh","db:3306","--","python","-m","uvicorn","FastAPI.main:app","--host","0.0.0.0","--port","8000"]
