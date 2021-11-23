from flask import session

_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]
_SORT_ORDER = {'Not Started': 0, 'Completed': 1}

def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    return session.get('items', _DEFAULT_ITEMS.copy())


def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    items = get_items()

    # Determine the ID for the item based on that of the highest in the list
    id = get_next_id()
    item = { 'id': id, 'title': title, 'status': 'Not Started' }

    # Add the item to the list
    items.append(item)
    items.sort(key=lambda val: _SORT_ORDER[val['status']])
    session['items'] = items

    return item


def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]
    updated_items.sort(key=lambda val: _SORT_ORDER[val['status']])
    session['items'] = updated_items

    return item

def remove_item(id):
    items = get_items()
    items = [item for item in items if item['id'] != id]
    session['items'] = items
    return

def get_next_id():
    items = get_items()
    if items.length == 0:
        return 1
    maximum_existing_id = max([item['id'] for item in items])
    return maximum_existing_id + 1