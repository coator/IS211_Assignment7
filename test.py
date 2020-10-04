import main
import unittest


class TestDiceTester(unittest.TestCase):

    def test_dice_roll(self):
        """Rolls dice roll and prints result along with seed"""
        dice = main.Dice()
        for x in range(0,6):
            dice.Roll()
        dice.RollStats()


if __name__ == '__main__':
    unittest.main()

