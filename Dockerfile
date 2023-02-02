FROM python:3.9-slim-bullseye

WORKDIR /app

COPY req.txt .

RUN pip install -r req.txt

COPY . .

ENTRYPOINT ["python", "main.py"]