class Item:
    def __init__(self, id: str, name: str, status: str = "To Do"):
        self.id = id
        self.name = name
        self.status = status
    
    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card["id"], card["name"], list["name"])