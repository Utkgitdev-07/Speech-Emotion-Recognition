# Use official Python image as base
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy required files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
