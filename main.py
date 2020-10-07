"""Pig game"""

from collections import Counter
import random


class CustomErrorExceptions:
    class ErrorPlayerIntInvalid(ValueError):
        pass


class Dice:
    def __init__(self):
        self.roll_amt = 0
        self.roll_list = []
        # self.rolllist is literally declaring that the item is = what the user puts in. why did it take me so long
        # to figure that out

    def __repr__(self):
        return self.roll_amt

    def RollStats(self):
        print('Current statistics for dice object {} are {}'.format(hex(id(self)), Counter(self.roll_list)))

    def Roll(self):
        """generates a new dice for the dice class"""
        result = random.choices((1, 2, 3, 4, 5, 6))
        self.roll_amt += 1
        self.roll_list.append(result[0])
        print('Dice result is {}'.format(result))
        return result[0]


class Player:
    def __init__(self, pname, pid, score=0):
        self.name = pname
        self.id = pid
        self.score = score

    def AddScore(self, score_addon):
        self.score = self.score + score_addon


"""
while True:
    player_amount = input('Please put in amount of players between 2 and 10')
    try:
        player_amount = int(player_amount)
    except:
        print('Invalid type used, must be a integer between 2 and 10.')
"""


class Game:
    def __init__(self, turn_count=0, player_amount=2):
        """create a game instance"""
        self.player_amount = player_amount
        self.pl = []
        self.turn_count = turn_count

    # TODO: Need to make main loop to purge any invalid player_amount entries before new game
    def newGame(self):
        if self.player_amount < 2 or self.player_amount > 10:
            raise CustomErrorExceptions.ErrorPlayerIntInvalid
        for player in range(0, self.player_amount):
            name = input('Please put in name for Player {}: '.format(player + 1))
            self.pl.append(Player(pname=name, pid=player))

    def gamePlay(self):
        victory = False
        while not victory:
            for player in range(0, self.player_amount):
                current_player = self.pl[player]
                if current_player.score > 99:
                    print("{} has won with a score of {}")
                    victory = True
                    return
                else:
                    self.gameRound(current_player)
                    self.turn_count += 1
                    print('next player')

    def gameRound(self, current_player):
        print("{}, it is your turn. You currently have {} points.".format(current_player.name, current_player.score))
        rollcount, scorecount, turn_end = 0, 0, False
        while turn_end is False:
            dice = Dice()
            result = dice.Roll()
            if result == 1:
                return
            else:
                scorecount += result
                rollcount += 1
                while not turn_end:
                    player_choice = input(
                        'Please choose "r" to roll or "h" to hold and end your turn '.format(current_player.name))
                    if player_choice == 'h':
                        current_player.AddScore(scorecount)
                        print('{} ends their turn with {} points.'.format(current_player.name,
                                                                          current_player.score))
                        return
                    if player_choice == 'r':
                        result = dice.Roll()
                        if result == 1:
                            return
                        else:
                            scorecount += result
                            rollcount += 1
                    else:
                        'Player {} Invalid selection, please try again '.format(current_player.name)
        return


def main():
    players = int(input('how many players between 2 and 10 '))
    current = Game(player_amount=players)
    current.newGame()
    current.gamePlay()


main()
