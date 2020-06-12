from room import Room
from player import Player
from item import Item
from item import Treasure

# Declare all the rooms


outside = Room("Outside Cave Entrance",
               "North of you, the cave mount beckons")
foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""")
overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")
narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""")
treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

# Link rooms together


outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow

# declaring player
player = Player("Shawn", outside)

# adding items to the rooms?
torch = Item("torch", "this gives off an immense amount of light")

treasure_chest = Treasure(
    "Treasure Chest", """This is full to the brim of gold and jewels. The entire thing looks like it might be worth quite a bit""", "100 gold")

outside.items.append(torch)
treasure.items.append(treasure_chest)

while True:

    print(f"You are currently in the {player.current_location}")

    cmd = input(
        "[n] moves north, [e] moves east, [s] moves south, [w] moves west \n Enter Command: ").split()

    cmd_list = {'n', 'e', 's', 'w'},
    cmd_list_i = {"i"}
    select = False

    if cmd[0] in ["n", "s", "e", "w"]:
        print(cmd)
        # check if the current room has a n_to attr
        if hasattr(player.current_location, f"{cmd[0]}_to"):
            # move player to that room
            player.current_location = getattr(
                player.current_location, f"{cmd[0]}_to")
        else:
            print("You cannot move that direction from this room")
    if len(cmd) == 2:
        if cmd[0] == "get":
            if len(player.current_location.items) == 0:
                print("There is nothing in the room to get")
            elif len(player.current_location.items) >= 1:
                res = player.items.insert(
                    0, player.current_location.items.pop())
                print(f"You now have {player.items[0]}")

        elif cmd[0] == "drop":
            if len(player.items) > 0:
                resdrop = player.current_location.items.insert(
                    0, player.items.pop())
                print(f" \n You have dropped your item. \n")

    elif cmd[0] == "i":
        player.inventory()

    elif cmd == "q":
        print("Thank you for playing!")
        break
