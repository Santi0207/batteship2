from model.coordinate import Coordinate
from model.ship import Ship


class ShipDistribution:
    def __init__(self,box: Coordinate, ship: Ship, orientation: bytes, state:str):
        self.box = box
        self.ship = ship
        self.orientation = orientation
        self.state = state

