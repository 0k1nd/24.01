from fastapi.testclient import TestClient
import os
from dotenv import load_dotenv


from main import app
load_dotenv()



client = TestClient(app)


def test_get_calltouch():
    siteId = int(os.getenv("SITE_ID"))
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
        "dateTo": dateTo,
        "withCallTags": True,
        "page": page,
        "limit": limit
    })
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert isinstance(data, dict)
    assert "page", "recordsTotal" in data
    assert isinstance(data["records"], list)