from model.list_DE import List_DE
from model.coordinate import Coordinate
from model.user import User

class Board:
    def __init__(self,data, id: int, cols: int, filas: int, player:User, listShip: List_DE, stateTable: bool,
                 shotsReceiver:Coordinate):
        self.id = id
        self.cols = cols
        self.filas = filas
        self.player = player
        self.listShip = listShip
        self.stateTable = stateTable
        self.shotsReceiver = data ['coordinate'] #duda como se coloca una lista 

