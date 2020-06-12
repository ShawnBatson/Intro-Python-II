# elif cmd in cmd_list and cmd == 'w':
#     try:
#         select = True
#         player.current_location = room[player.current_location].w_to.name
#     except:
#         print("You cannot move that direction from this room")
# elif cmd in cmd_list and cmd == 'e':
#     try:
#         select = True
#         player.current_location = room[player.current_location].e_to.name
#     except:
#         print("You cannot move that direction from this room")
# elif cmd in cmd_list and cmd == 's':
#     try:
#         select = True
#         player.current_location = room[player.current_location].s_to.name
#     except:
#         print("You cannot move that direction from this room")
# elif cmd in cmd_list and cmd == 'q':
#     print("See you next time!")
#     game = False

# if select == True:
#     if player.current_location == "Outside Cave Entrance":
#         player.current_location == "outside"
#     if player.current_location == "Foyer":
#         player.current_location == "foyer"
#     if player.current_location == "Grand Overlook":
#         player.current_location == "overlook"
#     if player.current_location == "Narrow Passage":
#         player.current_location == "narrow"
#     if player.current_location == "Treasure Chamber":
#         player.current_location == "treasure"

# player.current_location = player.current_location.lower()

# description = room[player.current_location].description

# print(
#     f"""\n Current Location: {player.current_location}, \n Description: {description} \n""")
# select = False


# Make a new player object that is currently in the 'outside' room.

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
# player.current_location = 'outside'
# if cmd == 'n':
#     if player.current_location.n_to is not None:
#         player.current_location = player.current_location.n_to
# elif cmd == 's':
#     if player.current_location.s_to is not None:
#         player.current_location = player.current_location.s_to
# elif cmd == 'e':
#     if player.current_location.e_to is not None:
#         player.current_location = player.current_location.e_to
# elif cmd == 'w':
#     if player.current_location.w_to is not None:
#         player.current_location = player.current_location.w_to
