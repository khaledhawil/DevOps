# Use a minimal base image
FROM alpine:3.14.2

# Set environment variables
ENV key=value APP_HOME=/app \ 
PORT=3000 \ 
NODE_ENV=production

# Use specific tags for your base image
LABEL maintainer="Your Name <youremail@example.com>" \
org.label-schema.name="my-app" \
org.label-schema.description="My App Description" \
org.label-schema.version="1.0.0"

# Use multiple layers
RUN apk add --no-cache nodejs npm
WORKDIR $APP_HOME
COPY package*.json ./
RUN npm install
COPY . .

# Use a health check
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:$PORT/health || exit 1

# Expose port and start the app
EXPOSE $PORT

CMD [ "npm", "start" ]

# Clean up after yourself
RUN apk del nodejs npm \ 
 && rm -rf /var/cache/apk/*

# Use a .dockerignore file
#COPY .dockerignore ./
