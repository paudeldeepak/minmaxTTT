import random


class Bot:
    def __init__(self,player):
        self.player = player

    def selectMoves(self,game):
        legalMoves = game.legalMoves()
        board = game.getBoard()

        move = 0

        for player in ["X","O"]:
            for moves in legalMoves:
                if 