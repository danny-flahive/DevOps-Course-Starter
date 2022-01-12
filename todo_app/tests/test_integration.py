from dotenv import load_dotenv, find_dotenv
from todo_app import app
import requests, os, pytest

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    test_app = app.create_app()
    with test_app.test_client() as client:
        yield client

def test_index_page(monkeypatch, client):
    monkeypatch.setattr(requests, 'request', get_lists_stub)
    response = client.get('/')
    #assert response.json()["cards"]["id"] == "1A"
    assert response.status_code == 200
    assert "Test card" in response.data.decode()

def test_remove(monkeypatch, client):
    monkeypatch.setattr(requests, 'request', get_lists_stub)
    response = client.get("/")
    #Check the card is actually on the page to start with
    assert "Test card" in response.data.decode()
    response = client.post("/remove/1A")
    #Test removing it works as expected
    assert "Test card" not in response.data.decode()
    

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data
    def json(self):
        return self.fake_response_data

def get_lists_stub(method, url, params, headers):
    test_board_id = os.environ.get('TRELLO_BOARD_ID')
    fake_response_data = None
    if method == "GET" and url == f'https://api.trello.com/1/boards/{test_board_id}/lists':
        fake_response_data = [{
        'id': '1',
        'name': 'To Do',
        'cards': [{'id': '1A', 'name': 'Test card', "desc": "Test"}]
        }]
    if method == "DELETE" and url == f"https://api.trello.com/1/cards/1A":
        fake_response_data = [{
        'id': '1',
        'name': 'To Do',
        'cards': [{}]
        }]
    return StubResponse(fake_response_data)