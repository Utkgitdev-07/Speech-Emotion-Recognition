# Use an official Python image as the base
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install system dependencies for PyAudio
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Set an environment variable to disable GPU
ENV CUDA_VISIBLE_DEVICES="-1"

# Use Gunicorn instead of Flask dev server
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
