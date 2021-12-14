class Item:
    def __init__(self, id: str, name: str, description: str = "", status: str = "To Do"):
        self.id = id
        self.name = name
        self.status = status
        self.description = description
    
    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card["id"], card["name"], card["desc"], list["name"])