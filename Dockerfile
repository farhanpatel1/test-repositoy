# Use a lightweight base image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy everything from your repo into the image
COPY . .

# Optionally, print the version file for verification
RUN cat VERSION || echo "No VERSION file found"

# Default command
CMD ["python3", "--version"]
