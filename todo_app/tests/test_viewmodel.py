import pytest
from todo_app.ViewModel import ViewModel

from todo_app.data.trello_items import get_items, remove_item, add_item

@pytest.fixture
def setup_lists():
    #Clear the board but save the original state
    original_items = get_items()
    for item in original_items:
        remove_item(item.id)
    #Add items
    add_item("Done Test", board="Done")
    add_item("Doing Test", board= "Doing")
    add_item("To Do Test", board="To Do")
    #Return items
    test_items = get_items()
    yield ViewModel(test_items)
    #Teardown: restore board to it's original state
    for item in test_items:
        remove_item(item.id)
    for item in original_items:
        add_item(item.name, item.description, item.status)

def test_pytestworks():
    assert(True)

def test_viewmodel_doing(setup_lists):
    assert len(setup_lists.doing) == 1
    assert setup_lists.doing[0].name == "Doing Test"
    with pytest.raises(IndexError):
        setup_lists.doing[1]


def test_viewmodel_todo(setup_lists):
    assert len(ViewModel.done) == 1
    assert ViewModel.done[0].name == "Done Test"
    with pytest.raises(IndexError):
        setup_lists.done[1]

def test_viewmodel_done(setup_lists):
    assert len(ViewModel.to_do) == 1
    assert ViewModel.doing[0].name == "To Do Test"
    with pytest.raises(IndexError):
        setup_lists.to_do[1]