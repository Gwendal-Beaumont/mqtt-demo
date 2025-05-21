FROM python:3.10-slim
WORKDIR /app
COPY app.py .
RUN pip install paho-mqtt
CMD ["python", "app.py"]
