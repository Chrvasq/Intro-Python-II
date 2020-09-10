from room import Room
from player import Player
import sys

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

# Make a new player object that is currently in the 'outside' room.
player = Player("Player 1", room["outside"])

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
def main():
    playing = True

    while playing:
        valid_directions = ('n', 'w', 's', 'e')
        connections = {
            'n': player.current_room.n_to if hasattr(player.current_room, "n_to") else "",
            's': player.current_room.s_to if hasattr(player.current_room, "s_to") else "",
            'e': player.current_room.e_to if hasattr(player.current_room, "e_to") else "",
            'w': player.current_room.w_to if hasattr(player.current_room, "w_to") else ""
        }

        print(player.current_room)

        cmd = input('''Enter a direction you would like to travel or Q to quit: ''').lower()

        if cmd == 'q':
            playing = False
        elif cmd not in valid_directions:
            print(f"\n{cmd} is an invalid command.")
        elif connections[cmd]:
            player.current_room = connections[cmd]
        else:
            print("\nThere's no exit in that direction.")

if __name__ == "__main__":
    main()
