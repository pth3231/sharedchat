# ---- Stage 1: Build ----
# Use a full Python image as the builder, which is necessary for compiling some packages
# Name this stage 'builder' for easy reference
FROM python:3.12-alpine3.22 AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create a virtual environment and set it up
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies from requirements.txt
WORKDIR /auth-service
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- Stage 2: Runtime ----
# Use a minimal Python image for the final, production-ready image
FROM python:3.12-alpine3.22

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Copy the virtual environment from the 'builder' stage
COPY --from=builder /opt/venv /opt/venv

# Make sure the new virtual environment is in the PATH
ENV PATH="/opt/venv/bin:$PATH"

# Set the working directory
WORKDIR /auth-service

# Copy the application source code from the host
COPY main.py .
COPY src src

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]