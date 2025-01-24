from fastapi.testclient import TestClient
import os

from .main import app


client = TestClient(app)


def test_get_calltouch():
    siteId = os.getenv("SITE_ID")
    clientApiId = os.getenv("CLIENTAPILD")
    dateFrom = '29/11/2024'
    dateTo = '29/11/2024'
    page = 3
    limit = 2
    response = client.get("/calltouch/", params={
        "siteId": siteId,
        "clientApiId": clientApiId,
        "dateFrom": dateFrom,
        "dateTo": dateTo,
        "page": page,
        "limit": limit
    })
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert isinstance(data, list)
    assert "callId" in data