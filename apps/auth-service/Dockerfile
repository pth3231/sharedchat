FROM python:3.10-slim

## Essential environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

## Work directory inside the docker container
WORKDIR /auth-service

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy source code to working directory
COPY . .

# Run setup.py to install dependencies
RUN pip install --no-cache-dir -e .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

