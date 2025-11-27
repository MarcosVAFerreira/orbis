# tests/test_api.py
import pytest
from src.api import app as flask_app

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as c:
        yield c

def test_health(client):
    rv = client.get('/health')
    assert rv.status_code == 200
    assert rv.json['status'] == 'ok'

def test_create_user_and_deposit(client):
    rv = client.post('/users', json={'username': 'bob', 'full_name': 'Bob Test'})
    assert rv.status_code == 200
    body = rv.json
    assert 'user_id' in body and 'account_id' in body

    acc = body['account_id']
    rv2 = client.post(f'/accounts/{acc}/deposit', json={'amount': 123.45})
    assert rv2.status_code == 200
    assert float(rv2.json['amount']) == 123.45
