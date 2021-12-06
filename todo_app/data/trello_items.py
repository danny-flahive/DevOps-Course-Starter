import os, requests

key = os.getenv("TRELLO_API_KEY")
token = os.getenv("TRELLO_API_TOKEN")
board = os.getenv("TRELLO_BOARD_ID")
headers = {"Accept" : "application/json"}

def get_items():
    global cards
    url = f"https://api.trello.com/1/boards/{board}/lists?key={key}&token={token}&cards=open"
    response = requests.request("GET", url, headers=headers).json()
    cards = [{}]
    cards.clear()
    for list in response:
        for card in list["cards"]:
            cards.append({"id" : card["id"], "title" : card["name"], "status" : list["name"]})
    return cards

def add_item(title: str):
    list_id = __get_list_id__("To Do")
    url = f"https://api.trello.com/1/cards?key={key}&token={token}&name={title}&idList={list_id}"
    print(requests.request("POST", url, headers=headers))

def complete_item(id: str):
    new_list_id = __get_list_id__("Done")
    url = f"https://api.trello.com/1/cards/{id}?key={key}&token={token}&idList={new_list_id}"
    requests.request("PUT", url, headers=headers)

def remove_item(id: str):
    url = f"https://api.trello.com/1/cards/{id}?key={key}&token={token}"
    requests.request("DELETE", url, headers=headers)

def __get_list_id__(name: str) -> str:
    url = f"https://api.trello.com/1/boards/{board}/lists?key={key}&token={token}"
    response = requests.request("GET", url, headers=headers).json()
    for list in response:
        if list["name"] == name:
            return list["id"]
    return None