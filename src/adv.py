from room import Room
from player import Player
from item import Item

# Declare all the rooms

sword = Item('sword', "it's literally a sword.")
bird = Item('bird', "tweet, tweet.")
skull = Item('skull', "I don't know either, dude.")
gold = Item('gold', "treasure")
cat = Item('cat', "I don't know either, dude.")

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [sword, ]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [skull, ]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [bird, cat]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [gold, ]),
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

    player = Player(name, room['outside'], [])

    print(f'\nWelcome {player.name}\n')

    user_input = ''

    print(f'{player.location}\n')
    print(f'{player.location.items}\n')

    while user_input != 'q':
        user_input = input('\nEnter a cardinal direction [N, E, S, W]:\t')

        if user_input.lower() == 'q':
            break
        elif user_input.upper() in ['N', 'S', 'E', 'W']:
            player.change_direction(user_input.upper())
            continue
        elif len(user_input.split(' ')) == 2:
            verb, object = user_input.split(' ')

            if verb in ['get', 'take']:
                # check to see if object exists
                import ipdb; ipdb.set_trace()
                if object in player.location.items:
                    player.items.append(player.location.items[f'{object}'])
                    player.location.remove(object)


if __name__ == '__main__':
    main()
