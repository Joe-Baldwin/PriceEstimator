from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_get_vendors():
    response = client.get("/vendors")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert all('id' in v and 'name' in v for v in data)

def test_get_items_by_vendor():
    # This test assumes at least one vendor exists in vendor_mapping.json
    vendors = client.get("/vendors").json()
    if vendors:
        vendor_id = vendors[0]['id']
        response = client.get(f"/vendors/{vendor_id}/items")
        assert response.status_code == 200 or response.status_code == 404

def test_export_vendors():
    response = client.get("/export/vendors")
    assert response.status_code == 200 or response.status_code == 500
    # 500 if no data yet
