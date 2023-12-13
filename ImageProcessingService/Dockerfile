# Use an official Python runtime as a parent image
FROM python:3.9-slim
LABEL authors="romainmarques & antoinelachaud"

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx git libglib2.0-0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 911

# Run app.py when the container launches
CMD ["python", "server.py"]
