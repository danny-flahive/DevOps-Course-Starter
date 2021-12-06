import os, requests
from todo_app.Item import Item

key = os.getenv("TRELLO_API_KEY")
token = os.getenv("TRELLO_API_TOKEN")
board = os.getenv("TRELLO_BOARD_ID")
headers = {"Accept" : "application/json"}

def get_items() -> list:
    url = f"https://api.trello.com/1/boards/{board}/lists?key={key}&token={token}&cards=open"
    response = requests.request("GET", url, headers=headers).json()
    cards = []
    for list in response:
        for card in list["cards"]:
            cards.append(Item.from_trello_card(card, list))
    return cards

def add_item(title: str, description: str) -> None:
    list_id = __get_list_id__("To Do")
    url = f"https://api.trello.com/1/cards?key={key}&token={token}&desc={description}&name={title}&idList={list_id}"
    print(requests.request("POST", url, headers=headers))

def complete_item(id: str) -> None:
    new_list_id = __get_list_id__("Done")
    url = f"https://api.trello.com/1/cards/{id}?key={key}&token={token}&idList={new_list_id}"
    requests.request("PUT", url, headers=headers)

def remove_item(id: str) -> None:
    url = f"https://api.trello.com/1/cards/{id}?key={key}&token={token}"
    requests.request("DELETE", url, headers=headers)

def __get_list_id__(name: str) -> str:
    url = f"https://api.trello.com/1/boards/{board}/lists?key={key}&token={token}"
    response = requests.request("GET", url, headers=headers).json()
    return next(list["id"] for list in response if list["name"] == name)