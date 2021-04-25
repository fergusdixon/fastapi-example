from fastapi.testclient import TestClient

from app.core.config import settings


def test_create_user_success(client: TestClient) -> None:
    response = client.post(f"{settings.API_V1_STR}/users", json={"name": "Test User"})
    assert response.status_code == 201
    data = response.json()
    assert data.get("name") == "Test User"
    assert data.get("id") > 0


def test_create_user_fail(client: TestClient) -> None:
    response = client.post(f"{settings.API_V1_STR}/users", json={"foo": "bar"})
    assert response.status_code == 422


def test_get_user(client: TestClient) -> None:
    response = client.post(f"{settings.API_V1_STR}/users", json={"name": "Test User 2"})
    assert response.status_code == 201
    data = response.json()
    user_id = data.get("id")

    user_response = client.get(f"{settings.API_V1_STR}/users/{user_id}")
    assert user_response.status_code == 200
    assert user_response.json().get("name") == "Test User 2"


def test_get_user_fail(client: TestClient) -> None:
    user_response = client.get(f"{settings.API_V1_STR}/users/-1")
    assert user_response.status_code == 404
    assert user_response.json().get("detail") == "User -1 not found."


def test_link_user_to_address(client: TestClient) -> None:
    user = client.post(f"{settings.API_V1_STR}/users", json={"name": "Test User 3"}).json()
    address = client.post(f"{settings.API_V1_STR}/addresses", json={"place": "Test Address 2"}).json()

    assert user
    assert address

    link_response = client.put(f"{settings.API_V1_STR}/users/{user['id']}/address/{address['id']}")
    assert link_response.status_code == 200

    user = client.get(f"{settings.API_V1_STR}/users/{user['id']}").json()
    assert isinstance(user.get("addresses"), list)
    assert len(user.get("addresses")) == 1
    assert user.get("addresses")[0]["id"] == address["id"]


def test_link_user_to_bad_address(client: TestClient) -> None:
    user = client.post(f"{settings.API_V1_STR}/users", json={"name": "Test User 3"}).json()
    link_response = client.put(f"{settings.API_V1_STR}/users/{user['id']}/address/-1")
    assert link_response.status_code == 404
    assert link_response.json().get("detail") == "Address -1 not found."


def test_link_bad_user_to_address(client: TestClient) -> None:
    link_response = client.put(f"{settings.API_V1_STR}/users/-1/address/1")
    assert link_response.status_code == 404
    assert link_response.json().get("detail") == "User -1 not found."
