from fastapi.testclient import TestClient

from app.core.config import settings


def test_create_address_success(client: TestClient) -> None:
    response = client.post(f"{settings.API_V1_STR}/addresses", json={"place": "Test Address"})
    assert response.status_code == 201
    data = response.json()
    assert data.get("place") == "Test Address"
    assert data.get("id") > 0


def test_create_address_fail(client: TestClient) -> None:
    response = client.post(f"{settings.API_V1_STR}/addresses", json={"foo": "bar"})
    assert response.status_code == 422


def test_get_address(client: TestClient) -> None:
    response = client.post(f"{settings.API_V1_STR}/addresses", json={"place": "Test Address 2"})
    assert response.status_code == 201
    data = response.json()
    address_id = data.get("id")

    address_response = client.get(f"{settings.API_V1_STR}/addresses/{address_id}")
    assert address_response.status_code == 200
    assert address_response.json().get("place") == "Test Address 2"


def test_get_address_fail(client: TestClient) -> None:
    address_response = client.get(f"{settings.API_V1_STR}/addresses/-1")
    assert address_response.status_code == 404
    assert address_response.json().get("detail") == "Address -1 not found."
