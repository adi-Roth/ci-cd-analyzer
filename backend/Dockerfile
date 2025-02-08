# First Stage: Build
FROM python:3.12 AS builder

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt -t /app/deps

# Copy source code
COPY . .

# Second Stage: Production
FROM python:3.12-slim

WORKDIR /app

# Copy dependencies from builder stage
COPY --from=builder /app/deps /app/deps
COPY --from=builder /app /app

# Set environment variables
ENV PYTHONPATH=/app/deps

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
