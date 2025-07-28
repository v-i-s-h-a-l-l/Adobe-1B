FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirement file
COPY requirements.txt .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Install torch separately first
RUN pip install --no-cache-dir torch==2.1.2+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html

# Remove torch from requirements.txt and install the rest
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the code
COPY . .

# Run the script
CMD ["python", "process_pdfs.py"]