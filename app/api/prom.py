"""OLD Prometheus Python Client Example"""
import random
import time
from prometheus_client import start_http_server, Summary, Counter, Gauge
from flask import Blueprint, redirect
from app.config import Config

metrics = Blueprint('metrics', __name__)

# Request processing time
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Temperature metrics
TEMPERATURE_GAUGE = Gauge('temperature_celsius', 'Current average temperature')
TEMPERATURE_REQUESTS = Counter('temperature_requests_total', 'Total temperature endpoint requests')
TEMPERATURE_ERRORS = Counter('temperature_errors_total', 'Total temperature endpoint errors')

# Cache metrics
CACHE_HITS = Counter('cache_hits_total', 'Total cache hits')
CACHE_MISSES = Counter('cache_misses_total', 'Total cache misses')

# Storage metrics
STORAGE_OPERATIONS = Counter('storage_operations_total',
                            'Total storage operations',
                            ['operation', 'status'])

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
