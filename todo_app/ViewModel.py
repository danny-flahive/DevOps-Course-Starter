from todo_app.Item import Item


class ViewModel:
    def __init__(self, items: list[Item]):
        self._items: list[Item] = items

    @property
    def items(self) -> list[Item]:
        return self._items
    
    @property
    def to_do(self) -> list[Item]:
        return [item for item in self._items if item.status == "To Do"]

    @property
    def doing(self) -> list[Item]:
        return [item for item in self._items if item.status == "Doing"]

    @property
    def done(self) -> list[Item]:
        return [item for item in self._items if item.status == "Done"]
