FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY youless_exporter.py .

CMD [ "python", "youless_exporter.py" ]
