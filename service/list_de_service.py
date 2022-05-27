from model.list_de import List_DE
from model.ship import Ship
from model.ship_distribution import ShipDistribution

class ListDEService:
    def __init__(self):
        self.list_de = List_DE()

    def list(self):
        return self.list_de.list()

    def add(self,data: Ship):
        ship_dist = ShipDistribution(data)
        self.list_de.add(ship_dist)
        return {"message":"Barco adicionado exitosamente"}

    def add_to_star(self,data:Ship):
        ship_dist = ShipDistribution(data)
        self.list_de.add_to_star(ship_dist)
        return {"message":"Barco adicionado exitosamente"}

    def clone_list(self):
        return self.list_de.clone_list().list()
