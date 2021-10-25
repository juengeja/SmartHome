from abc import abstractmethod


class Device():

    @abstractmethod
    def getroom(self):
        pass

    @abstractmethod
    def setroom(self, room):
        pass
