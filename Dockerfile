FROM python:3:10
###adding filename

##Adding one more line

ENV PYTHONDONTWRITERBYTECODE=1\
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y\
    build-essential\
    curl\
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -e .

EXPOSE 5000

CMD ["python", "app.py"]
