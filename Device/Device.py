from abc import abstractmethod


class Device():

    @abstractmethod
    def getroom(self):
        """Get the room, in which this device is located."""
        pass

    @abstractmethod
    def setroom(self, room):
        """Set a room for this device, in which it is located."""
        pass
