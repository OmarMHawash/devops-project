"""OLD Prometheus Python Client Example"""
import random
import time
from prometheus_client import start_http_server, Summary
from flask import Blueprint, redirect
from app.config import Config

metrics = Blueprint('metrics', __name__)

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

@metrics.route('/')
def index():
    """Health Check"""
    start_http_server(Config.PROMETHEUS_PORT)
    # Generate some requests.
    while True:
        process_request(random.random())
        return redirect(f'http://127.0.0.1:{Config.PROMETHEUS_PORT}')
