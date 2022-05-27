from .ship_distribution import ShipDistribution

class Node_DE:
    def __init__(self,data:ShipDistribution):
        self.data = data
        self.next = None
        self.previous = None

