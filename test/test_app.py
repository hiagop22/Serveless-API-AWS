import secrets


def generate_random_token(length=32):
    """Generate a random token."""
    return secrets.token_hex(length)


def test_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, from aws lambda"}


def test_incorrect_credentials(client):
    username = "invalid_username"
    password = "invalid_password"
        
    response = client.post("/token",
                            data={"username": username,
                                  "password": password},
                                  )
    print(response.json())    
    assert response.status_code == 401


def test_authenticated_endpoint(header_auth, client):
    headers = header_auth
        
    response = client.get("/users/me",headers=headers)

    print(response.json())    
    assert response.status_code == 200


def test_unauthenticated_endpoint(client):
    token = generate_random_token()
    headers = {"Authorization": f"Bearer {token}"}

    try:    
        client.post("/users/me", headers=headers)
    except Exception as e:
        assert type(e) is Exception
        assert str(e) == "Unauthorized"