import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture
def client():
    """Provide a clean TestClient for each test."""
    original_activities = {
        name: {
            key: value[:] if isinstance(value, list) else value
            for key, value in details.items()
        }
        for name, details in activities.items()
    }

    try:
        yield TestClient(app)
    finally:
        activities.clear()
        activities.update(original_activities)
