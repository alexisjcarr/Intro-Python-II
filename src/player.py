# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def change_direction(self, direction):
        # import ipdb; ipdb.set_trace()
        try:
            if direction == 'N':
                self.location = self.location.n_to
            elif direction == 'E':
                self.location = self.location.e_to
            elif direction == 'S':
                self.location = self.location.s_to
            elif direction == 'W':
                self.location = self.location.w_to
            print(f'\n{self.location}')
        except AttributeError:
            print(f'\nThere is no room {direction} of this room.')

    def __str__(self):
        return f'{self.name} is in {self.location}'
