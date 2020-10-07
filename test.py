import main
import unittest


class TestGame(unittest.TestCase):

    def test_game_invalid_player_amt(self):
        """Initializes the wtong amount of players causing a loop"""
        g = main.Game(player_amount=11)
        self.assertRaises(main.CustomErrorExceptions.ErrorPlayerIntInvalid,g.newGame)
        g = main.Game(player_amount=1)
        self.assertRaises(main.CustomErrorExceptions.ErrorPlayerIntInvalid,g.newGame)

    def test_game_run(self):
        g = main.Game(player_amount=2)


if __name__ == '__main__':
    unittest.main()

