# here is a simple doker file with flask app

# Specify the base image
# FROM python:latest
FROM python:latest

# Set the working directory for subsequent instructions

WORKDIR /app
#WORKDIR /app

# Copy  requirements.txt file to the Docker image
COPY requirements.txt .
#COPY requirements.txt .


# Install dependencies
#RUN pip install -r requirements.txt 
RUN pip install -r requirements.txt
# Copy python file to  docker image 
COPY app.py .


# Expose port 5000 to the host machine
EXPOSE 5000


# Set the default command to run when the Docker container starts
CMD python app.py 

