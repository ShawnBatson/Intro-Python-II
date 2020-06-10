# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    hp = 20

    def __init__(self, name, current_location):
        self.name = name
        self.current_location = current_location

    def __str__(self):
        output = f"Hello {self.name}!"
        return output

    def __repr__(self):
        return f"self.name = {self.name} "


class Warrior(Player):

    hp = 40

    def __init__(self, name, current_location, skills):
        super().__init__(name, current_location)
        self.skills = ["Slash", "Bludgeon",
                       "Charge", "Stalwart", "Riposte", "Parry"]


class Priest(Player):

    hp = 30

    def __init__(self, name, current_location, skills):
        super().__init__(name, current_location)
        self.skills = ["Bludgeon", "Stand Fast", "Pray (group heal)",
                       "Heal (Single Target)", "Retreat", "Lay on Hands"]


class Mage(Player):

    def __init__(self, name, current_location, skills):
        super().__init__(name, current_location)
        self.skills = ["Flame Bolt", "Ice Spike",
                       "Elemental Maelstrom", "Storm Cloud", "Acid Splash", "Retreat"]
