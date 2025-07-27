FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy everything
COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the script
CMD ["python", "process_collections.py"]
