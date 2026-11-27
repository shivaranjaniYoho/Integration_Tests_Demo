
def test_home_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to Integration Testing API"
    }


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_create_customer(client):
    response = client.post(
        "/customers/",
        json={
            "name": "Arun",
            "email": "arun@example.com"
        }
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Arun"
    assert response.json()["email"] == "arun@example.com"


def test_get_all_customers(client):
    client.post(
        "/customers/",
        json={
            "name": "Arun",
            "email": "arun@example.com"
        }
    )

    response = client.get("/customers/")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_customer(client):
    create_response = client.post(
        "/customers/",
        json={
            "name": "Arun",
            "email": "arun@example.com"
        }
    )

    customer_id = create_response.json()["id"]

    response = client.get(f"/customers/{customer_id}")

    assert response.status_code == 200
    assert response.json()["name"] == "Arun"


def test_update_customer(client):
    create_response = client.post(
        "/customers/",
        json={
            "name": "Arun",
            "email": "arun@example.com"
        }
    )

    customer_id = create_response.json()["id"]

    response = client.put(
        f"/customers/{customer_id}",
        json={
            "name": "Arun Kumar",
            "email": "arunkumar@example.com"
        }
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Arun Kumar"


def test_delete_customer(client):
    create_response = client.post(
        "/customers/",
        json={
            "name": "Arun",
            "email": "arun@example.com"
        }
    )

    customer_id = create_response.json()["id"]

    response = client.delete(f"/customers/{customer_id}")

    assert response.status_code == 204


def test_customer_not_found(client):
    response = client.get("/customers/999")

    assert response.status_code == 404


def test_duplicate_email(client):
    client.post(
        "/customers/",
        json={
            "name": "Arun",
            "email": "arun@example.com"
        }
    )

    response = client.post(
        "/customers/",
        json={
            "name": "Priya",
            "email": "arun@example.com"
        }
    )

    assert response.status_code == 409


def test_invalid_customer_data(client):
    response = client.post(
        "/customers/",
        json={
            "name": "A",
            "email": "not-an-email"
        }
    )

    assert response.status_code == 422
