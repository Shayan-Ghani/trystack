import pytest

#to create an instance of our programme
from trystack import create_app

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    return app.test_client()
