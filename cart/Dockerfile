FROM python:3.9-slim

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

# OpenTelemetry environment variables for zero-code instrumentation
ENV OTEL_EXPORTER_OTLP_ENDPOINT=http://52.23.211.13:4317
ENV OTEL_SERVICE_NAME="cart"  # Replace with each service name, e.g., 'items', 'cart', 'payment'

EXPOSE 5002  # Adjust according to each service's port (5001, 5002, 5003)

CMD ["opentelemetry-instrument", "python", "app.py"]
