from abc import ABC, abstractmethod


class FridgeHandler(ABC):

    @abstractmethod
    def set_successor(successor):
        pass

    @abstractmethod
    def request_add_item(item, amount):
        pass

    @abstractmethod
    def request_available_item(item, amount):
        pass
