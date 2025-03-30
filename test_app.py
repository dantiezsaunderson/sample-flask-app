import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_home_page(client):
    rv = client.get('/')
    assert b'Welcome' in rv.data

def test_about_page(client):
    rv = client.get('/about')
    assert b'About' in rv.data

def test_contact_form(client):
    rv = client.post('/contact', data=dict(email='test@test.com', message='Hello'))
    assert b'Sent' in rv.data

def test_time_endpoint(client):
    rv = client.get('/time')
    assert rv.status_code == 200