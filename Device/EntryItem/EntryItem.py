from abc import abstractmethod
from Device.Device import Device


class EntryItem(Device):

    @abstractmethod
    def islocked(self):
        pass

    @abstractmethod
    def isopen(self):
        pass

    @abstractmethod
    def setlocked(self, locked):
        pass

    @abstractmethod
    def setopen(self, open):
        pass
