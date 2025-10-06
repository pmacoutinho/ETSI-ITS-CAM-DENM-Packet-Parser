FROM python:3.11-slim

# Install tshark (needed by pyshark)
RUN apt-get update && \
    apt-get install -y tshark && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements first (for better layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY main.py .

ENTRYPOINT ["python", "main.py"]
