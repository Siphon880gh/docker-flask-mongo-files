
# Flask-MongoDB Docker Project
By Weng Fei Fung

![Last Commit](https://img.shields.io/github/last-commit/Siphon880gh/docker-flask-mongo-files/main)
<a target="_blank" href="https://github.com/Siphon880gh" rel="nofollow"><img src="https://img.shields.io/badge/GitHub--blue?style=social&logo=GitHub" alt="Github" data-canonical-src="https://img.shields.io/badge/GitHub--blue?style=social&logo=GitHub" style="max-width:8.5ch;"></a>
<a target="_blank" href="https://www.linkedin.com/in/weng-fung/" rel="nofollow"><img src="https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin&labelColor=blue" alt="Linked-In" data-canonical-src="https://img.shields.io/badge/LinkedIn-blue?style=flat&amp;logo=linkedin&amp;labelColor=blue" style="max-width:10ch;"></a>
<a target="_blank" href="https://www.youtube.com/@WayneTeachesCode/" rel="nofollow"><img src="https://img.shields.io/badge/Youtube-red?style=flat&logo=youtube&labelColor=red" alt="Youtube" data-canonical-src="https://img.shields.io/badge/Youtube-red?style=flat&amp;logo=youtube&amp;labelColor=red" style="max-width:10ch;"></a>

## TLDR
This is a containerized flask that connects to the host machine's mongo and can read files that can be changed outside of docker without needing to rebuild the docker image. As a consequence, port 5001 is exposed and mapped for flask, host.docker.internal is the connection string for Mongo when inside docker, and the current folder is mapped as virtual.

Born out of a need, I decided to templatize this process so I can deploy Flask-Mongo apps quickly.

## Overview

This project consists of a containerized Flask application designed to interact seamlessly with a MongoDB instance on the host machine. It is specifically configured to allow file modifications outside of the Docker environment without the need to rebuild the Docker image.

## Features

- **Host Machine MongoDB Connection**: The Flask app connects to the MongoDB service running on the host machine. This is achieved by using `host.docker.internal` as the MongoDB connection string when the application is running inside a Docker container.
- **File Accessibility**: Files within the current folder are mapped as a volume in Docker. This setup allows for external modifications of these files without needing to rebuild the Docker image.
- **Port Mapping**: Port 5001 is exposed and mapped to the host to facilitate access to the Flask application.

## Configuration Details

- **MongoDB Connection**: The application automatically detects whether it is running inside a Docker container and adjusts the MongoDB connection string accordingly. It uses `host.docker.internal` for Docker environments and `localhost` for non-Docker environments.
- **Port Exposure**: Port 5001 is configured in the Dockerfile and mapped during the container's runtime for external accessibility.
- **Volume Mapping**: The current directory is mapped to a specific path inside the container, enabling live file updates from the host machine.

## Running the Application

To run this application:

1. **Build the Docker Image** (if not already built):
   ```
   docker build -t flask-mongo-app .
   ```
2. **Run the Docker Container**:
   ```
   docker run -p 5001:5001 -v $(pwd):/app flask-mongo-app
   ```

   This command maps port 5001 and the current directory as a volume to the Docker container.

## Additional Notes

- Ensure MongoDB is running on the host machine and is configured to accept connections.
- Modify the MongoDB connection configuration in the Flask application if your setup deviates from the standard port or requires additional parameters.
