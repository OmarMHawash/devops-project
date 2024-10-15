"""Unit tests for routes"""
from main import app
from app.config import Config

def test_status():
    """Test status"""
    response = app.test_client().get("/")
    assert response.status_code == 200, response.text
    assert response.json["Status"] == "OK", response.text

def test_version():
    """Test version"""
    response = app.test_client().get("/version")
    assert response.status_code == 200, response.text
    assert response.json["Version"] == Config.APP_VERSION, response.text

def test_temperature():
    """Test temperature"""
    response = app.test_client().get("/api/temperature")
    assert response.status_code == 200, response.text
    assert "Average temperature" in response.json, response.text
    assert isinstance(response.json["Average temperature"], (int, float)), response.text
