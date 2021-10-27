from Device.Fridge.BeverageCooler import BeverageCooler
from Device.Fridge.KitchenFridge import KitchenFridge
from Device.Fridge.Minibar import Minibar


class FridgeChain:

    def __init__(self):
        self.link1 = Minibar(5, 5, 3, 2)
        self.link2 = BeverageCooler(10, 10, 10, 0)
        self.link3 = KitchenFridge(15, 15, 15, 10)

    def standardChain(self):
        self.link1.set_successor(self.link2)
        self.link2.set_successor(self.link3)

    def reverseChain(self):
        self.link3.set_successor(self.link2)
        self.link2.set_successor(self.link1)
