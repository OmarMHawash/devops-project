"""WIP Test fixtures"""
import pytest
from main import app

@pytest.fixture
def client():
    """A test client for the app."""
    app.config['TESTING'] = True
    yield app.test_client()
