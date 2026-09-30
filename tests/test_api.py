from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_explain_demo():
    response = client.post("/api/v1/explain", json={"language":"python","code":"def add(a,b): return a+b"})
    assert response.status_code == 200
    assert "Language: python" in response.json()["result"]

def test_sql_demo():
    response = client.post("/api/v1/sql", json={"request":"show latest records"})
    assert response.status_code == 200
    assert "ORDER BY created_at" in response.json()["result"]
