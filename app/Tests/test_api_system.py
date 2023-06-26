from fastapi.testclient import TestClient
from main import app

from database.sys_db import SysDb
from database.data_models import Tag, Role, TagUpdate


client = TestClient(app)

def test_update_tags():
    # Mock the database operation and expected response
    class MockSysDb:
        def update_tags(self, tags_id: int, tags: TagUpdate):
            # Simulate the database update operation and return a mock response
            return {"id": tags_id, "name": tags.name}

    # Replace the original SysDb instance with the mock object
    app.dependency_overrides[SysDb] = MockSysDb

    # Define the request payload
    payload = {
        "name": "Updated Tag"
    }

    # Send a PUT request to the endpoint
    response = client.put("/tags/1", json=payload)

    # Assert the response status code and content
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Updated Tag"}

    # Remove the mock dependency override
    del app.dependency_overrides[SysDb]


