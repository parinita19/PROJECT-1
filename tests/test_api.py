from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_run_endpoint_success():
    response = client.post("/run", params={"task": "Please format /data/format.md with prettier 3.4.2"})
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["status"] == "success"

def test_read_endpoint_not_found():
    response = client.get("/read", params={"path": "nonexistent.txt"})
    assert response.status_code == 404