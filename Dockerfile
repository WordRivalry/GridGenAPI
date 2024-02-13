# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.8-slim-buster as base

# Set the working directory in the container
WORKDIR /usr/src/app

COPY requirements.txt ./
COPY data ./data
COPY src ./src

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# RUN pip install gunicorn

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV NAME World

CMD ["gunicorn", "-b", ":8080", "src.app:app"]