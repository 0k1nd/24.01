from fastapi.testclient import TestClient

from .main import app


client = TestClient(app)


def test_get_calltouch():
    response = client.get()