import unittest
from parameterized import parameterized

from player import Player
from room import Room


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.mock_room = {
            'outside':  Room("Outside Cave Entrance", "North of you, the cave\
                 mount beckons"),
            'foyer':    Room("Foyer", "Dim light filters in from the south. \
                Dusty passages run north and east."),
        }
        self.mock_player = Player('test', self.mock_room['outside'])
        self.mock_room['outside'].n_to = self.mock_room['foyer']

    @parameterized.expand([
        ('North', 'N', 'Foyer'),
        ('East', 'E', 'Outside Cave Entrance'),
        ('South', 'S', 'Outside Cave Entrance'),
        ('West', 'W', 'Outside Cave Entrance'),
    ])
    def test_change_direction_changes_to_right_direction(
        self,
        _test_name,
        direction,
        expected_location,
    ):
        self.mock_player.change_direction(direction)
        actual_location, _ = str(self.mock_player.location).split(':')
        self.assertEqual(actual_location, expected_location)


if __name__ == '__main__':
    unittest.main()
