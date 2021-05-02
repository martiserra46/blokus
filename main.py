from game import Game
from player import *

if __name__ == '__main__':
    game = Game()
    players = [HumanPlayer('A'), RandomComputerPlayer('B'), RandomComputerPlayer('C'), RandomComputerPlayer('D')]
    game.play(players)