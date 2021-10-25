from abc import abstractmethod
from Device.Device import Device


class EntryItem(Device):

    @abstractmethod
    def islocked(self):
        """Get boolean: Is the EntryItem locked?"""
        pass

    @abstractmethod
    def isopen(self):
        """Get boolean: Is the EntryItem open?"""
        pass

    @abstractmethod
    def setlocked(self, locked):
        """Set boolean: Lock or unlock the EntryItem"""
        pass

    @abstractmethod
    def setopen(self, open):
        """Set boolean: Open or close the EntryItem"""
        pass
