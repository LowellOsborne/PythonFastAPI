# Use Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your project files into the container
COPY . .

# Expose FastAPI's default port
EXPOSE 8000

# Start the FastAPI app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
