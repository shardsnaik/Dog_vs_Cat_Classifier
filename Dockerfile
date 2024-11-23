# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy only the requirements file to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

ENV DAGSHUB_USERNAME=sharadnaik001
ENV DAGSHUB_TOKEN=f86ef673fbadc6b8a3188c34cd7218030c6b1f05

# Expose the port (optional, for documentation purposes)
# EXPOSE 80

# Run the main application when the container launches
CMD ["python", "main_file.py"]
