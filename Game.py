import numpy as np

class Game:

    def __init__(self):
        self.board = [[0 for i in range(3)] for j in range(3)]

    def __repr__(self):
        pass
        
    def turn(self,row,col, player):
        if player == 2:
            player = 4 # this is a weird idea but it makes victory validation quicker.
        self.board[row][col] = player
    
    @property
    def board(self):
        return self.board()

    @property
    def winner(self):
        #if someone won return winner else return false
        if np.sum(self.board[0]) == 12 or np.sum(self.board[1]) == 12 or np.sum(self.board[2]) == 12 or (12 in np.sum(self.board, axis=0)): #or diagonal
            pass

if __name__ == "__main__":
    pass

