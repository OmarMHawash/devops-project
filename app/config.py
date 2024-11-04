"""APP CONFIGURATION"""
import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv('REDIS_HOST'))
class Config:
    """APP CONFIGURATION"""
    ENV = os.getenv('ENVIRONMENT', 'development')
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', '5000'))
    APP_VERSION = "0.0.1"
    REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', '60'))
    PROMETHEUS_PORT = int(os.getenv('PROMETHEUS_PORT', '8000'))

class OpenSense:
    """OPENSENSE API CONFIGURATION"""
    API_URL = os.getenv('API_URL', "https://api.opensensemap.org")
    GET_BOXES_PREFIX = "/boxes"
    BOXES_OFFSET_HOURS = int(os.getenv('BOXES_OFFSET_HOURS', '-1'))

class TestConfig():
    """TEST CONFIGURATION"""
    TESTING = True

class Valkey:
    """VALKEY CONFIGURATION"""
    HOST = os.getenv('REDIS_HOST', "localhost")
    PORT = int(os.getenv('REDIS_PORT', '6379'))
    DB = int(os.getenv('REDIS_DB', '0'))
    EXP = int(os.getenv('VALKEY_EXP', '300'))

class MinIO:
    """MINIO CONFIGURATION"""
    ENDPOINT = os.getenv('MINIO_ENDPOINT', "minio-service:9000")
    ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY')
    SECRET_KEY = os.getenv('MINIO_SECRET_KEY')
    BUCKET_NAME = os.getenv('MINIO_BUCKET_NAME', "sensebox-data")
    SECURE = os.getenv('MINIO_SECURE', 'False').lower() == 'true'
