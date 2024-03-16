import sys
from pathlib import Path

ROOT = Path(__file__).parents[1]
API_ROOT = ROOT / "api"

if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))

from app import app


import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def api_credentials():
    return {
        "username": "hiago",
        "password": "naruto",
    }

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def header_auth(api_credentials, client):
    username = api_credentials["username"]
    password = api_credentials["password"]
        
    response = client.post("/token",
                            data={"username": username,
                                    "password": password},
                                    )
    assert response.status_code == 200

    token = response.json().get("access_token")
    
    assert token is not None

    return {"Authorization": "Bearer %s" % token}