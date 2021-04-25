from typing import Any

from behave import given, then, use_fixture, use_step_matcher, when
from faker import Faker

from app.core.config import settings
from app.tests.features.fixtures import test_client

use_step_matcher("re")

fake = Faker()


@given("a user's id, and 2 addresses ids")
def create_one_user_two_addresses(context: Any) -> None:
    """
    :type context: behave.runner.Context
    """
    client = use_fixture(test_client, context=context)
    context.user_name = fake.name()
    response = client.post(f"{settings.API_V1_STR}/users", json={"name": context.user_name})
    assert response.status_code == 201
    context.user_id = response.json()["id"]

    context.address_name_one = fake.address()
    response = client.post(f"{settings.API_V1_STR}/addresses", json={"place": context.address_name_one})
    assert response.status_code == 201
    context.address_id_one = response.json()["id"]

    context.address_name_two = fake.address()
    response = client.post(f"{settings.API_V1_STR}/addresses", json={"place": context.address_name_two})
    assert response.status_code == 201
    context.address_id_two = response.json()["id"]


@when("we we link them")
def link_addresses(context: Any) -> None:
    """
    :type context: behave.runner.Context
    """
    client = use_fixture(test_client, context=context)

    response = client.put(f"{settings.API_V1_STR}/users/{context.user_id}/address/{context.address_id_one}")
    assert response.status_code == 200
    response = client.put(f"{settings.API_V1_STR}/users/{context.user_id}/address/{context.address_id_two}")
    assert response.status_code == 200


@then("we see the entities are linked")
def check_address_are_linked(context: Any) -> None:
    """
    :type context: behave.runner.Context
    """
    client = use_fixture(test_client, context=context)

    response = client.get(f"{settings.API_V1_STR}/users/{context.user_id}")
    assert response.status_code == 200

    assert response.json()
    assert len(response.json().get("addresses", [])) == 2
    assert response.json().get("id") == context.user_id
    assert response.json()["addresses"][0]["id"] in [context.address_id_one, context.address_id_two]
    assert response.json()["addresses"][0]["place"] in [context.address_name_one, context.address_name_two]
    assert response.json()["addresses"][1]["id"] in [context.address_id_one, context.address_id_two]
    assert response.json()["addresses"][1]["place"] in [context.address_name_one, context.address_name_two]
