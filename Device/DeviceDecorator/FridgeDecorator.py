from abc import ABC

from Device.Fridge.FridgeChain import FridgeChain
from Device.Fridge.FridgeHandler import FridgeHandler


# Abstract Base Decorator
class FridgeDecorator(FridgeHandler, ABC):
    _fridgeHandler: FridgeHandler

    def __init__(self, fridgeHandler: FridgeHandler, fridgeChain: FridgeChain):
        self.fridgeChain = fridgeChain
        self._fridgeHandler = fridgeHandler

    @property
    def fridgeHandler(self):
        return self._fridgeHandler

    def request_add_item(self, item, amount):
        return self._fridgeHandler.request_add_item(item, amount)

    def request_available_item(self, item, amount):
        return self._fridgeHandler.request_available_item(item, amount)


# Lightweight Decorators
class AddItemsDecorator(FridgeDecorator):

    def set_successor(successor):
        pass

    def add_item(self, item, amount):
        self.fridgeChain.reverseChain()
        print("recommended storage: ")
        self.fridgeHandler.request_add_item(item, amount)


class GetItemsDecorator(FridgeDecorator):
    def set_successor(successor):
        pass

    def get_item(self, item, amount):
        self.fridgeChain.standardChain()
        self.fridgeHandler.request_available_item(item, amount)
