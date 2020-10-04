"""Pig game"""

from collections import Counter
import random



class Dice:
    def __init__(self):
        self.roll_amt = 0
        self.roll_list = []
        #self.rolllist is literally declaring that the item is = what the user puts in. why did it take me so long
        #to figure that out

    def __repr__(self):
        return self.roll_amt

    def RollStats(self):
        return 'Current statistics for dice object {} are {}'.format(id(self), Counter(self.roll_list))


    def Roll(self):
        """generates a new dice for the dice class"""
        dice = (1, 2, 3, 4, 5, 6)
        result = (random.choices(dice))
        self.roll_amt+=1
        self.roll_list.append(result)
        print('Dice result is {}'.format(result))
        return result

class Player:
    pass


class Game:
    def __init__(self, player, dice):
        self.player = player
        self.dice = dice

    def newGame(self, *playeramt):
        pl = []
        for player in playeramt:
            pl.append({player: 0})
        return pl


    def gamePlay(self, playerlist):
