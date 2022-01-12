FROM python:3-slim

ADD . /app
WORKDIR /app
CMD ["python", "app.py"]
