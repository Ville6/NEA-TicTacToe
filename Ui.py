from abc import ABC, abstractmethod
from Game import Game
from pprint import pprint as pp

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        pass

class Terminal(Ui):
    def __init__(self):
        pass

    def run(self):
        game = Game()
        board = game.board
        player = 1
        print("Player 1 has x")
        print("Player 2 has o")
        
        while game.winner() == 0:
            print(f"player {player} to turn")
            print("   1    2    3")
            print("1" + str(board[0]))
            print("2" + str(board[1]))
            print("3" + str(board[2]))
            square = input("input row and col in format 'xy'")
            if game.turn(int(square[1]) - 1, int(square[0]) - 1, player):
                player += 1
                if player == 3:
                    player = 1

        result = game.winner()
        if result == 3:
            print("Draw")
        else:
            print(f"Player {result} won.")
        
        print("   1    2    3")
        print("1" + str(board[0]))
        print("2" + str(board[1]))
        print("3" + str(board[2]))

