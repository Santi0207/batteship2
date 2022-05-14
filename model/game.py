from model.board import Board
class Game:
    def __init__(self, id:int, boardPlayer1:Board, boardPlayer2:Board, numberShip:any, turn : bytes, hitsplayer1:int,
                 hitsplayer2:int):
        self.id = id
        self.boardPlayer1 = boardPlayer1
        self.boardPlayer2 = boardPlayer2
        self.numberShip = numberShip
        self.turn = turn
        self.hitsplayer1 = hitsplayer1
        self.hitsplayer2 = hitsplayer2