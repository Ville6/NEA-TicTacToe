from abc import ABC, abstractmethod
from Game import Game
from pprint import pprint as pp

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        self._game = Game()

    def run(self):
        pass

class Terminal(Ui):
    def __init__(self):
        self._game = Game()

    def run(self):
        player = 1
        print("Player 1 has x")
        print("Player 2 has o")
        
        while self._game.winner() == 0:
            print(f"player {player} to turn")
            print("   1    2    3")
            print("1" + str(self._game.board[0]))
            print("2" + str(self._game.board[1]))
            print("3" + str(self._game.board[2]))
            square = input("input row and col in format 'xy'")
            if self._game.turn(int(square[1]) - 1, int(square[0]) - 1, player):
                player += 1
                if player == 3:
                    player = 1
            else:
                print("Illegal move.")

            print("")

        print("   1    2    3")
        print("1" + str(self._game.board[0]))
        print("2" + str(self._game.board[1]))
        print("3" + str(self._game.board[2]))

        result = self._game.winner()
        if result == 3:
            print("Draw")
        else:
            print(f"Player {result} won.")
