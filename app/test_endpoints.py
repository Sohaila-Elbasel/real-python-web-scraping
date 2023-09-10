from fastapi.testclient import TestClient
from app.main import app
from scraper.scraping import get_realpython_response

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

def test_update_data():
    response = client.get('/update')
    assert response.json() == {'message': 'Well Done'}

def test_get_realpython_response():
    get_realpython_response()