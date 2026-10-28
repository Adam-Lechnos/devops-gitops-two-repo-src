import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_hello_world_default(client):
    """Test the root route with the default environment fallback message."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"<h1>Hello, World!</h1>" in response.data

def test_hello_world_custom_env(client, monkeypatch):
    """Test that the root route successfully reads the CUSTOM_MESSAGE environment variable."""
    # Temporarily set the environment variable for this test
    monkeypatch.setenv("CUSTOM_MESSAGE", "Enterprise GitOps Test!")
    
    response = client.get("/")
    assert response.status_code == 200
    assert b"<h1>Enterprise GitOps Test!</h1>" in response.data

def test_greet_user_api(client):
    """Test the JSON API endpoint returns the correct message and status code."""
    response = client.get("/api/greet")
    assert response.status_code == 200
    
    # Verify JSON payload structure
    json_data = response.get_json()
    assert json_data["status"] == "success"
    assert "Hello from src repo!!" in json_data["message"]