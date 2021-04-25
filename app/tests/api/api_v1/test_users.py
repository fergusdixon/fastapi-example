from fastapi.testclient import TestClient

from app.core.config import settings


def test_create_user_success(client: TestClient) -> None:
    response = client.post(f"{settings.API_V1_STR}/users", json={
        "name": "Test User"
    })
    assert response.status_code == 201
    data = response.json()
    assert data.get("name") == "Test User"
    assert data.get("id") > 0


def test_create_user_fail(client: TestClient) -> None:
    response = client.post(f"{settings.API_V1_STR}/users", json={
        "foo": "bar"
    })
    assert response.status_code == 422


def test_get_user(client: TestClient) -> None:
    response = client.post(f"{settings.API_V1_STR}/users", json={
        "name": "Test User 2"
    })
    assert response.status_code == 201
    data = response.json()
    user_id = data.get("id")

    user_response = client.get(f"{settings.API_V1_STR}/users/{user_id}")
    assert user_response.status_code == 200
    assert user_response.json().get("name") == "Test User 2"
