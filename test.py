import main
import unittest


class TestDiceTester(unittest.TestCase):

    def test_dice_roll(self):
        """Rolls dice roll and prints result along with seed"""
        dice = main.Dice()
        for x in range(0,6):
            dice.Roll()
        dice.RollStats()

class TestGame(unittest.TestCase):

    def test_game_invalid_player_amt(self):
        """Initializes the wtong amount of players causing a loop"""
        # TODO: check assignment6 for the proper way to do this.
        TestGame.assertRaises(main.CustomErrorExceptions.ErrorPlayerIntInvalid(), main.Game, 1)






if __name__ == '__main__':
    unittest.main()

