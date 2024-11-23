# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Expose the Flask default port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]