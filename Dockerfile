# Use the official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code to the working directory
COPY . /app

# Install the Python dependencies
RUN pip install -r requirements.txt

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "main:app", "--reload"]