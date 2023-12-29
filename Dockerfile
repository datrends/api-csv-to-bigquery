# Use the official Python base image
FROM python:3.9-slim

# Copy the application code to the working directory
COPY . /app

# Set the working directory inside the container
WORKDIR /app

# Install the Python dependencies
RUN pip install -r requirements.txt

# Expose the port on which the application will run
EXPOSE 80

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "main:app", "--reload"]