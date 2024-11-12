FROM nginx:1.21

# Install the OpenTelemetry NGINX module
RUN apt-get update && \
    apt-get install -y wget unzip && \
    wget https://github.com/open-telemetry/opentelemetry-cpp-contrib/releases/download/v1.3.0/nginx-otel-linux-x64.zip && \
    unzip nginx-otel-linux-x64.zip -d /usr/lib/nginx/modules/ && \
    rm nginx-otel-linux-x64.zip && \
    apt-get remove -y wget unzip && \
    apt-get autoremove -y && \
    apt-get clean

# Copy NGINX configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
