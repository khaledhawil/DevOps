# Use an official Python image

FROM python:3.9-slim-buster

# Set the working directory to /app

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app 

# install ant nedded packges specified in req.txt file

RUN pip install --no-cache-dir  -r req.txt


# make a port 80 available to the world outside this  container 

EXPOSE 80 

# RUN app.py when the container starting

CMD ["python", "app.py"]


