from fastapi import FastAPI
from fastapi.testclient import TestClient
from cdapi.CCLE_web_service import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}