import pytest, requests
from todo_app.Item import Item
from todo_app.ViewModel import ViewModel

from todo_app.data.trello_items import get_items

@pytest.fixture
def viewmodel_test():
    items = [Item("1", "To Do Test", status="To Do"), Item("2", "Doing Test", status="Doing"), Item("3", "Done Test", status="Done")]
    return ViewModel(items)

def test_pytest_works():
    assert(True)

def test_viewmodel_doing(viewmodel_test):
    assert len(viewmodel_test.doing) == 1
    assert viewmodel_test.doing[0].name == "Doing Test"
    with pytest.raises(IndexError):
        viewmodel_test.doing[1]


def test_viewmodel_done(viewmodel_test):
    assert len(viewmodel_test.done) == 1
    assert viewmodel_test.done[0].name == "Done Test"
    with pytest.raises(IndexError):
        viewmodel_test.done[1]

def test_viewmodel_todo(viewmodel_test):
    assert len(viewmodel_test.to_do) == 1
    assert viewmodel_test.to_do[0].name == "To Do Test"
    with pytest.raises(IndexError):
        viewmodel_test.to_do[1]
    
def test_get_items(monkeypatch):
    monkeypatch.setattr(requests, "request", stub)
    items = get_items()
    assert len(items) == 4
    assert items[0].name == "Test 1A"
    assert items[1].name == "Test 2A"
    assert items[2].name == "Test 1B"
    assert items[3].name == "Test 2B"


def stub(method, url, params, headers):
    return StubResponse()

class StubResponse:
    def json(x):
        response = [{"id" : "A", "name" : "Test A", "cards" : [{"id" : "1", "name" : "Test 1A", "desc" : ""}, {"id" : "2", "name" : "Test 2A", "desc" : ""}]}, {"id" : "B", "name" : "Test B", "cards" : [{"id" : "1", "name" : "Test 1B", "desc" : ""}, {"id" : "2", "name" : "Test 2B", "desc" : ""}]}]
        return response