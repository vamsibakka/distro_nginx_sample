FROM python:3.9-slim

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

# OpenTelemetry environment variables for zero-code instrumentation
ENV OTEL_EXPORTER_OTLP_ENDPOINT="http://52.23.211.13:4317"
ENV OTEL_SERVICE_NAME="items" 

EXPOSE 5001  

CMD ["opentelemetry-instrument", "python", "app.py"]
