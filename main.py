"""Pig game"""

import argparse
import random


class CustomErrorExceptions:
    class ErrorPlayerIntInvalid(ValueError):
        pass


class Dice:
    def __init__(self):
        self.roll_amt = 0
        self.roll_list = []
        self.dice_seed_list = []

    def __repr__(self):
        return self.roll_amt

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


def victory_check(current_player, result):
    if current_player.score + result > 99:
        print("Player {} has won with a score of {}".format(current_player.name, result + current_player.score))
        game_over()


class Game:
    def __init__(self, player_amount=2):
        """create a game instance"""
        self.player_amount = player_amount
        self.pl = []
        self.turn_count = 1
        self.dice_count = 0
        self.random_seed = 0

    def game_state_tracker(self, dice_counter=0, turn_counter=0):
        self.turn_count += turn_counter
        self.dice_count += dice_counter

    def newGame(self):
        if self.player_amount < 2 or self.player_amount > 10:
            raise CustomErrorExceptions.ErrorPlayerIntInvalid
        for player in range(0, self.player_amount):
            self.pl.append(Player(pname=player + 1, pid=player))

    def gamePlay(self):
        while True:
            for player in range(0, self.player_amount):
                current_player = self.pl[player]
                print("_____________________________")
                print("|Now it is player {}'s turn  |".format(current_player.name))
                print("_____________________________")
                victory_check(current_player, result=0)
                self.gameRound(current_player)

    def gameRound(self, current_player):
        score_count, turn_end = 0, False
        dice = Dice()
        while turn_end is False:
            self.game_state_tracker(1, 0)
            result = dice.Roll()
            if result == 1:
                print("Player {},You rolled a 0 and your turn is over".format(current_player.name))
                return
            else:
                score_count += result
                victory_check(current_player, result=score_count)
                print(
                    "Player {}, it is your turn. Your score is {} points. You currently have a possible score of"
                    " {}".format(
                        current_player.name,
                        current_player.score, current_player.score + score_count))
                player_choice = None
                while player_choice is None:
                    player_choice = input(
                        'Please choose "r" to roll or "h" to hold and end your turn: '.format(current_player.name))
                    if player_choice == 'h':
                        current_player.AddScore(score_count)
                        print('{} ends their turn with {} points.'.format(current_player.name,
                                                                          current_player.score))
                        return
                    if player_choice == 'r':
                        continue
                    else:
                        player_choice = None


def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--playerint", default=2, help="Enter the amount of players in the game", type=int)
    args = parser.parse_args()
    return args.playerint


def game_over():
    while True:
        decision = input("play again? (y or n) :")
        if decision == 'y':
            main()
        if decision == 'n':
            print("goodbye!")
            exit()
        else:
            pass


def main():
    players = argparser()
    current = Game(player_amount=players)
    current.newGame()
    current.gamePlay()


main()
