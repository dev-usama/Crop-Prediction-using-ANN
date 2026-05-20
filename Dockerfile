# Use an official, lightweight Python image
FROM python:3.11-slim

# Prevent Python from writing .pyc files and buffer outputs for cleaner logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install basic system build dependencies required for compiling certain packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file first to take advantage of Docker's layer caching
COPY requirements.txt .

# Installing Python Packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the all of the project (app.py, models, scalers, encoders)
COPY . .

# Gunicorn Port
EXPOSE 7860

# Run Gunicorn Server
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]