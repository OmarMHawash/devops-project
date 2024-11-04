# Devops Lifecycle Project - HiveBox

<img src="https://img.shields.io/badge/python-3.11.8-blue" alt="python"> <img src="https://img.shields.io/badge/flask-2.3.2-red" alt="flask"> <img src="https://img.shields.io/badge/redis-7.4.1-pink" alt="redis"> <img src="https://img.shields.io/badge/minio-7.2.10-green" alt="minio"> <img src="https://img.shields.io/badge/docker-24.0.5-darkblue" alt="k8s">

## Overview

This project uses Flask API that interfaces with Redis for caching and MinIO for object storage. It is designed for seamless deployment on a Kubernetes cluster, leveraging Kind for efficient local development and testing.

## Table of Contents

1. [Flask API](#flask-api)
2. [Testing](#testing)
3. [Available Endpoints](#available-endpoints)
4. [CI/CD Pipelines](#cicd-pipelines)
5. [Kubernetes Setup](#kubernetes-setup)

---

## Flask API

### Directory Structure

The project is organized into a standard flask structure for the ease of development and maintainability.The main entry point is `main.py`, while the API logic in `app/api/routes.py`. Helper functions are encapsulated in `app/helpers`, and application configuration settings are managed in `app/config.py`.

```
/app
  /api
    routes.py
    prom.py
  /helpers
    cache.py
    storage.py
    utils.py
    routes.py
  /static
    sample_data.json
main.py
```

### other required files:

.env:
shows all the environment variables that are required to run the application, theres a sample file in the root directory.
.dockerignore and gitignore:
these files are used to exclude certain files and directories from the docker build process.

### local setup steps:

1. python 3.11.8 or newer installed
2. create a virtual envoriment: `python -m venv venv`
3. activate env then install required packages:
   `pip install -r requirements`
4. run via either:

- default python testing/development `python -m main.py`

- uwsgi for production puropses:
  NOTE: this is not included with requirements file, since it requires a bigger python image
  `uwsgi --http 127.0.0.1:5000 --wsgi-file main.py --callable app`

access via http://127.0.0.1:5000

## Testing

### Linting and Unit Testing

linting is enforced both locally and on CI pipeline before any changes are pushed to the main repository branch, utilizing Hadolint. Additionally, unit tests are conducted using pytest, allowing for robust validation of the API endpoints and overall application functionality.

---

## Available Endpoints

### Base Endpoints

- **Health Check:**
  - `/` or `/health`: Verify that the application is running smoothly.
- **Version Information:**

  - `/version`: Retrieve the current version of the application.
    - **Sample Response:**
      ```json
      {
        "Version": "0.0.1"
      }
      ```

- **Metrics:**
  - `/metrics`: Access Prometheus metrics to monitor application performance and health.

### API Endpoints

- **Average Temperature:**
  the data is cached in Redis for 5 minutes, since its an expensive operation to perform every time.
  - `/temperature`: Fetch the average temperature recorded by all SenseBoxes.
    - **Sample Response:**
      ```json
      {
        "Average temperature": 33.5,
        "status": "Hot"
      }
      ```
- **Data Storage:**
  - `/store`: (Work in Progress) This endpoint is designed to cache current sensor data to MinIO storage, facilitating easy retrieval and management of data.

---

## CI/CD Pipelines

### Branch Management

The **main** branch is reserved for production-ready code, while the **dev** branch is dedicated to ongoing development.

When changes are pushed to the **dev** branch, no immediate actions are triggered. However, upon the creation of a pull request, a continuous integration (CI) pipeline is initiated to validate the code. Successful execution leads to merging into the **main** branch.

Also, any changes pushed directly to the **main** branch trigger a continuous deployment (CD) pipeline, ensuring that updates are promptly delivered to production.

### CI Pipeline Jobs

- Python environment and installs necessary packages.
- Runs linting and unit tests to ensure code quality.
- Performs security scanning with Terrascan to identify potential vulnerabilities.
- Builds the Docker image for deployment.

### CD Pipeline Jobs

- Pushes the built Docker image to Docker Hub for distribution.
- Creates a new GitHub release, marking the latest version of the application.

---

## Kubernetes Setup

This project is set up to run smoothly on a **Kubernetes** cluster, utilizing **Kind** for local testing and development.

### Architecture Overview

- **Master Node and Worker Nodes:** The cluster consists of a master node that manages the system and multiple worker nodes that handle application workloads. This setup allows for efficient resource management and easy scaling.

### Service Deployment

- **Flask API:** The Flask API is deployed as a highly available service with multiple replicas. This ensures that the application can handle high traffic and maintain performance.
- **Redis and MinIO:** These services are also deployed:
  - **Redis:** Used for caching to speed up data retrieval.
  - **MinIO:** Provides object storage for data management.

### Data Management

- **Persistent Storage:** currently, each of redis and MinIO are deployed with one replica each. this ensures presistence and availability of data. although, it is recommended to have multiple replicas for redundancy and scalability, but requires more complex setup.

### Configuration Management

- **ConfigMaps:** Used for managing environment variables.
- **Secrets:** Used for storing sensitive information securely.
