# Use the official Python image as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first for better caching
COPY requirements.txt /app/

# Install the required dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the Django project code to the container
COPY . /app/
