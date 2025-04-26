# Use an official Python image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file in the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Set environment variables
ENV FLASK_RUN_HOST=0.0.0.0 

# Expose port
EXPOSE 5000

# Run the app
CMD [ "flask", "run" ]