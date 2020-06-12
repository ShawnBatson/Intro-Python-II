from player import Player
from item import Item


class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.n_to = None
        self.items = []

    def __str__(self):
        output = f"{self.name}: {self.description}\n\n "
        if len(self.items) != 0:
            output += f"You also see {self.items[0]}. "
        else:
            output += f"You see nothing else of interest \n"
        if self.s_to:
            output += "To the south is: " + self.s_to.name + '\n'
        if self.e_to:
            output += "To the east is: " + self.e_to.name + '\n'
        if self.w_to:
            output += "To the west is: " + self.w_to.name + '\n'
        if self.n_to:
            output += "To the north is: " + self.n_to.name + '\n'

        return output
