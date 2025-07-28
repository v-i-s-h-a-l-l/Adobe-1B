FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirement file separately to leverage Docker cache
COPY requirements.txt .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Install torch first (since it requires a special index)
RUN pip install --no-cache-dir torch==2.1.2+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html

# Remove torch line from requirements.txt, then:
# Install remaining Python dependencies
RUN pip install --no-cache-dir \
    sentence-transformers==2.2.2 \
    pdfplumber==0.10.3

# Copy the rest of the code
COPY . .

# Run the script
CMD ["python", "process_collections.py"]
