from room import Room

from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

game = True

# Make a new player object that is currently in the 'outside' room.

player = Player("Shawn", "outside")
print(f"You are currently in the {player.current_location} room")
print(f"You see as follows: {room[player.current_location].description}")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while game:
    cmd = input(
        """[n] moves north, [e] moves east, [s] moves south, [w] moves west""")

    cmd_list = ['n', 'e', 's', 'w', 'q'],
    select = False

    if cmd in cmd_list and cmd == 'n':
        try:
            select = True
            player.current_location = room[player.current_location].n_to.name
        except:
            print("You cannot move that direction from this room")
    elif cmd in cmd_list and cmd == 'w':
        try:
            select = True
            player.current_location = room[player.current_location].w_to.name
        except:
            print("You cannot move that direction from this room")
    elif cmd in cmd_list and cmd == 'e':
        try:
            select = True
            player.current_location = room[player.current_location].e_to.name
        except:
            print("You cannot move that direction from this room")
    elif cmd in cmd_list and cmd == 's':
        try:
            select = True
            player.current_location = room[player.current_location].s_to.name
        except:
            print("You cannot move that direction from this room")
    elif cmd in cmd_list and cmd == 'q':
        print("See you next time!")
        game = False
        break

    if select == True:
        if player.current_location == "Outside Cave Entrance":
            player.current_location == "outside"
        if player.current_location == "Foyer":
            player.current_location == "foyer"
        if player.current_location == "Grand Overlook":
            player.current_location == "overlook"
        if player.current_location == "Narrow Passage":
            player.current_location == "narrow"
        if player.current_location == "Treasure Chamber":
            player.current_location == "treasure"

        player.current_location = player.current_location.lower()

        description = room[player.current_location].description

        print(
            f"""\n Current Location: {player.current_location}, \n Description: {description} \n""")
        select = False
