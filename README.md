### installation steps:

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

for development must:
have hadolint setup
lint files before pushing

## for kubernetes setup:

- setup docker, kind, kubectl

- create kind cluster:

`kind create cluster --config k8s/kind-config.yaml`

apply kubernetes resources:

- Create MinIO secret
  kubectl apply -f k8s/minio-secret.yaml

- Deploy Redis
  kubectl apply -f k8s/redis.yaml

- Deploy MinIO
  kubectl apply -f k8s/minio.yaml

- Deploy Flask API
  kubectl apply -f k8s/flask-api.yaml

- Deploy Ingress rules
  kubectl apply -f k8s/ingress.yaml
