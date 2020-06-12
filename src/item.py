class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}, {self.description}"

    def get(self):
        return f"You pick up a {self.name}"

    def drop(self):
        return f"You drop a {self.name}"
