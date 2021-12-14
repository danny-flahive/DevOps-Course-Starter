import os, requests
from todo_app.Item import Item

board = os.getenv("TRELLO_BOARD_ID")
headers = {"Accept" : "application/json"}

def get_items() -> list:
    url = f"https://api.trello.com/1/boards/{board}/lists"
    params = _get_auth_params()
    params["cards"] = "open"
    response = requests.request("GET", url, params=params, headers=headers).json()
    cards = []
    for list in response:
        for card in list["cards"]:
            cards.append(Item.from_trello_card(card, list))
    return cards

def add_item(title: str, description: str) -> None:
    url = f"https://api.trello.com/1/cards"
    params = _get_auth_params()
    params["desc"] = description
    params["name"] = title
    params["idList"] = _get_list_id("To Do")
    print(requests.request("POST", url, params=params, headers=headers))

def complete_item(id: str) -> None:
    url = f"https://api.trello.com/1/cards/{id}"
    params = _get_auth_params()
    params["idList"] = _get_list_id("Done")
    requests.request("PUT", url, params=params, headers=headers)

def remove_item(id: str) -> None:
    url = f"https://api.trello.com/1/cards/{id}"
    params = _get_auth_params()
    requests.request("DELETE", url, params=params, headers=headers)

def _get_list_id(name: str) -> str:
    url = f"https://api.trello.com/1/boards/{board}/lists"
    params = _get_auth_params()
    response = requests.request("GET", url, params=params, headers=headers).json()
    return next(list["id"] for list in response if list["name"] == name)

def _get_auth_params() -> dict:
    return {"key" : os.getenv("TRELLO_API_KEY"), "token" : os.getenv("TRELLO_API_TOKEN")}