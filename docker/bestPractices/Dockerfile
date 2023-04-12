# Use a small base image
FROM alpine:3.13

# Set the working directory
WORKDIR /app

# Create a non-root user
RUN adduser -D myuser
USER myuser

# Install dependencies 
# Cleaning up temporary files with --no-cache-dir
RUN apk add --no-cache python3 py3-pip
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Set environment variables
ENV FLASK_APP=app.py

# Expose the port
EXPOSE 5000

# Start the application
CMD ["flask", "run", "--host=0.0.0.0"]