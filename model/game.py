from model.board import Board
from .user import User
from .list_de import List_DE

class Game:
    def __init__(self, player1:User, player2:User,ship_list:List_DE, id:int):
        self.id = id
        self.player1 = player1
        self.player2 = player2
        self.numberShip = ship_list.cont
        self.turn = 0
        self.hitsplayer1 = 0
        self.hitsplayer2 = 0
        self.board_player1=None
        self.board_player2=None
        self.__create_board(ship_list)



    def __create_board(self,ship_list:List_DE):
        size = 0
        if self.numberShip < 10:
            size = 10
        elif self.numberShip < 20:
            size = 20
        elif self.numberShip < 30:
            size = 30

        self.board_player1=Board(1,size,size,self.player1,ship_list)
        self.board_player2=Board(2,size,size,self.player2,ship_list.clone_list())