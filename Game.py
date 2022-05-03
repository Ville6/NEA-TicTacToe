import numpy as np

class Game:
    def __init__(self):
        self._board = [[0 for i in range(3)] for j in range(3)]
        self._real_board = [[' ' for i in range(3)] for j in range(3)]

    def __repr__(self):
        pass
        
    def turn(self,row,col, player):
        #return true if valid move, return false otherwise
        if self._board[row][col] == 0:
            if player == 1:
                self._real_board[row][col] = 'x'
            else:
                self._real_board[row][col] = 'o'

            player = player ** 2 # this is a weird idea but it makes victory validation quicker.
            self._board[row][col] = player
            return True
        else:
            return False

    def winner(self):
        #if someone won return winner else return 0
        if np.sum(self._board[0]) == 3 or np.sum(self._board[1]) == 3 or np.sum(self._board[2]) == 3 or (3 in np.sum(self._board, axis=0)) or self._board[0][0]+self._board[1][1]+self._board[2][2] == 3 or self._board[0][2]+self._board[1][1]+self._board[2][0] == 3:
            return 1 #player 1 won
        elif np.sum(self._board[0]) == 12 or np.sum(self._board[1]) == 12 or np.sum(self._board[2]) == 12 or (12 in np.sum(self._board, axis=0)) or self._board[0][0]+self._board[1][1]+self._board[2][2] == 12 or self._board[0][2]+self._board[1][1]+self._board[2][0] == 12:
            return 2 #player 2 won
        elif 0 not in self._board[0] and 0 not in self._board[1] and 0 not in self._board[2]: 
            return 3
        else:
            return 0

    @property
    def board(self):
        return self._real_board

if __name__ == "__main__":
    pass

