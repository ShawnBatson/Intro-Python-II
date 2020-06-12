

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, name, current_location):
        self.name = name
        self.current_location = current_location
        self.items = []

    def __str__(self):
        output = f"Hello {self.name}!"
        return output

    def __repr__(self):
        return f"self.name = {self.name} "

    def inventory(self):
        print("You are carrying: ")
        for item in self.items:
            print(item.name + "\n")
