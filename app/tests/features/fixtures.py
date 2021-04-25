from behave import fixture
from fastapi.testclient import TestClient

from app.main import app


# -- FIXTURE: Use generator-function
@fixture
def test_client(context, timeout=30, **kwargs):
    with TestClient(app) as c:
        yield c
