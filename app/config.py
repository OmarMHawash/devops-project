"""APP CONFIGURATION"""

class Config:
    """APP CONFIGURATION"""
    DEBUG_MODE = True
    HOST = '127.0.0.1'
    PORT = 5000
    APP_VERSION = "0.0.1"
    REQUEST_TIMEOUT = 60 # in seconds
    PROMETHEUS_PORT = 8000

class OpenSense:
    """OPENSENSE API CONFIGURATION"""
    API_URL = "https://api.opensensemap.org"
    GET_BOXES_PREFIX = "/boxes"
    BOXES_OFFSET_HOURS = -1

class TestConfig():
    """TEST CONFIGURATION"""
    TESTING = True
