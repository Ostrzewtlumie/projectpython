<<<<<<< HEAD
FROM python:2.7-slim

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD ["python", "scr.py"]
=======
# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
>>>>>>> 313f45766c02a4fd79728bc2b4bf1c915a8d9aea
