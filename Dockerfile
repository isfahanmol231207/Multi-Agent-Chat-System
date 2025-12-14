# ---------------- Dockerfile ----------------
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Step 1: Copy only the requirements file first
COPY requirements.txt .

# Step 2: Install dependencies (ensuring this layer runs)
RUN pip install --no-cache-dir -r requirements.txt

# Step 3: Copy the rest of the project files
COPY . .

# Default command
CMD ["python", "main.py"]