from fastapi.testclient import TestClient
import pytest

from src.services import quaggy_manager
from src.main import app

client = TestClient(app)

@pytest.mark.parametrize(
        "quaggy_id", 
        [
            0,
            512,
        ]
)
def test_quaggy_get_schedule_now(quaggy_id):
    response = client.get(f"/v2/quaggy/get_schedule_now/{quaggy_id}")
    assert response.status_code == 200
    #assert response.json() == {"msg": "Hello World"}

@pytest.mark.parametrize(
        "quaggy_id", 
        [
            10000
        ]
)
def test_quaggy_get_schedule_now_not_found(quaggy_id):
    response = client.get(f"/v2/quaggy/get_schedule_now/{quaggy_id}")
    assert response.status_code == 404