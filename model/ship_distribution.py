from model.ship import Ship

class ShipDistribution:
    def __init__(self, ship: Ship):
        self.places = []
        self.ship = ship
        self.orientation = 0
        self.state = "FREE"



