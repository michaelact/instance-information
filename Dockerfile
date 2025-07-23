# Use official Python image as a base
FROM python:3.13-slim

# Upgrade system packages
RUN apt-get update \
    && apt-get upgrade -y \
    && groupadd -r app \
    && useradd -m -r -g app app \
    && apt-get install -y --no-install-recommends \
        procps \
        curl \
        ca-certificates \
        cron \
    && rm -rf /var/lib/apt/lists/* \
    && service cron stop

# Set environment variables for security
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Use a non-root user for security
USER app

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY --chown=app:app requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY --chown=app:app main.py .

# Expose port
EXPOSE 8080

# Start the application
CMD ["python", "main.py"]
