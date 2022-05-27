from model.list_de import List_DE
from model.user import User

class Board:
    def __init__(self, id: int, cols: int, rows: int, player:User, ship_list: List_DE):
        self.id = id
        self.cols = cols
        self.rows = rows
        self.player = player
        self.ship_list = ship_list
        self.stateBoard = False
        self.shotsReceiver = []

    def valide_shoot(self,x:int, y:int):
        pass
