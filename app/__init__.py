"""Main App Module"""
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app
from app.api.routes import api, main
from app.config import TestConfig

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_object(TestConfig)
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(main)
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/metrics': make_wsgi_app()
    })
    return app
