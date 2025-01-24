from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI
import requests

app = FastAPI()


# class CallToush(BaseModel):
#     siteId: int
#     clientApiId: str
#     dateFrom: str
#     dateTo: str
#     pages: int
#     limit: int
    

@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/calltouch/")
def get_calltouch(
    siteId: int,
    clientApiId: str,
    dateFrom: str,
    dateTo: str,
    page: int,
    limit: int
):
    url = f'https://api.calltouch.ru/calls-service/RestAPI/{siteId}/calls-diary/calls'
    params = {
        "clientApiId": clientApiId,
        "dateFrom": dateFrom,
        "dateTo": dateTo,
        "page": page,
        "limit": limit
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)