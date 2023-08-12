import pytest
from app_mod import app


def test_hello_world():
    app.config['TESTING'] = True
    client = app.test_client()
    result = client.get('/')
    assert b'Hello World!' == result.data
