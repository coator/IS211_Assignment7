import main
import unittest


class TestDiceTester(unittest.TestCase):

    def test_dice_roll(self):
        """Rolls dice roll and prints result along with seed"""
        dice = main.Dice
        dice.Roll()

