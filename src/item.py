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


class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value

    def __str__(self):
        return f"{self.name}, {self.description}, worth: {self.value}"

    def get(self):
        return f"""You have found the treasure! It looks to be worth quite a bit! \n You see a {self.name}, {self.description}, it looks to be worth {self.value}"""
