"""Main App Module"""
from flask import Flask
from app.api.routes import api, main

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(main)
    return app
