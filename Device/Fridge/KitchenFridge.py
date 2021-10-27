from Device.Fridge.FridgeHandler import FridgeHandler


class KitchenFridge(FridgeHandler):

    def __init__(self, waterCapacity, colaCapacity, waterCount, colaCount):
        self._successor = None
        self._colaCount = colaCount
        self._waterCount = waterCount
        self._colaCapacity = colaCapacity
        self._waterCapacity = waterCapacity

    def set_successor(self, successor):
        self._successor = successor

    def request_add_item(self, item, amount):
        fridge = "kitchen fridge"
        if item == "water":
            newWaterCount = self._waterCount + amount
            addableAmount = self._waterCapacity-self._waterCount
            restAmount = amount-addableAmount
            if newWaterCount > self._waterCapacity:
                print(str(addableAmount) + " water bottles should be stored in: " + fridge)
                self._successor.request_add_item(item, restAmount)
            else:
                print(str(addableAmount) + " water bottles should be stored in: " + fridge)

        if item == "cola":
            newColaCount = self._colaCount + amount
            addableAmount = self._colaCapacity-self._colaCount
            restAmount = amount-addableAmount
            if newColaCount > self._colaCapacity:
                print(str(addableAmount) + " cola bottles should be stored in: " + fridge)
                self._successor.request_add_item(item, restAmount)
            else:
                addableAmount = self._colaCapacity-self._colaCount
                print(str(addableAmount) + " cola bottles should be stored in: " + fridge)

    def request_available_item(self, item, amount):
        fridge = "kitchen fridge"
        if item == "water":
            if amount < self._waterCount:
                print(str(self._waterCount) + " water bottles are available in: " + fridge)
            else:
                self._successor.request_available_item(item, amount)
        if item == "cola":
            if amount <= self._colaCount:
                print(str(self._colaCount) + " cola bottles are available in: " + fridge)
            else:
                print(str(self._colaCount) + " cola bottles are available in: " + fridge)
                self._successor.request_available_item(item, amount)