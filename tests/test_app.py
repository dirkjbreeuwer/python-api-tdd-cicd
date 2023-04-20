import pytest
from flask.testing import FlaskClient

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.resolve()))

from app import app

@pytest.fixture
def client() -> FlaskClient:
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_task(client):
    # Replace with a valid task ID after implementing the API
    task_id = 1
    response = client.get(f'/tasks/{task_id}')
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert response.json['id'] == task_id


def test_create_task(client):
    new_task = {
        'title': 'Test task',
        'description': 'This is a test task',
        'due_date': '2023-04-30T23:59:59Z'
    }
    response = client.post('/tasks', json=new_task)
    assert response.status_code == 201
    assert isinstance(response.json, dict)
    assert response.json['title'] == new_task['title']

def test_update_task(client):
    # Replace with a valid task ID after implementing the API
    task_id = 1
    updated_task = {
        'title': 'Updated test task',
        'completed': True
    }
    response = client.put(f'/tasks/{task_id}', json=updated_task)
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert response.json['title'] == updated_task['title']
    assert response.json['completed'] == updated_task['completed']

def test_delete_task(client):
    # Replace with a valid task ID after implementing the API
    task_id = 1
    response = client.delete(f'/tasks/{task_id}')
    assert response.status_code == 204

