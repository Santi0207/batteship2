from model.node_de import Node_DE
from .ship_distribution import ShipDistribution

class List_DE:
    def __init__(self):
        self.head = None
        self.cont = 0

    def add(self,data:ShipDistribution):
        if self.head == None:
            self.head = Node_DE(data)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            new_node = Node_DE(data)
            temp.next = new_node
            new_node.previous = temp
        self.cont += 1

    def add_to_star(self,data:ShipDistribution):
        if self.head == None:
            self.head = Node_DE(data)
        else:
            self.head.previous= Node_DE(data)
            self.head.previous.next = self.head
            self.head = self.head.previous
        self.cont += 1

    def list(self):
        list = []
        temp = self.head
        while temp != None:
            list.append(temp.data)
            temp = temp.next
        return list

    def clone_list(self):
        list = List_DE ()
        temp = self.head
        while temp != None:
            list.add(temp.data)
            temp = temp.next
        return list