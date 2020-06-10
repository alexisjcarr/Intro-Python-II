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


def main():
    name = input('What is your name?\t')

    player = Player(name, room['outside'])

    print(f'\nWelcome {player.name}\n')

    user_input = ''

    print(player.location)

    while user_input != 'q':
        user_input = input('\nEnter a cardinal direction [N, E, S, W]:\t')

        if user_input.lower() == 'q':
            break
        elif user_input.upper() == 'N' or user_input.upper() == 'E' or \
                user_input.upper() == 'S' or user_input.upper() == 'W':
            player.change_direction(user_input.upper())
            continue


if __name__ == "__main__":
    main()
