"""WIP Unit tests configuration"""

def test_status(client):
    """Test status"""
    response = client.get("/status")
    assert response.status_code == 200, response.text
    assert response.json["Status"] == "OK", response.text

def test_version(client):
    """Test version"""
    response = client.get("/version")
    assert response.status_code == 200, response.text
    # assert response.json["Version"] == Config.client_VERSION, response.text

def test_temperature(client):
    """Test temperature"""
    response = client.get("/api/temperature")
    assert response.status_code == 200, response.text
    assert response.json["Average temperature"] is not None, response.text
