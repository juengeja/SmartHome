from abc import abstractmethod
from Device.Device import Device


class Light(Device):

    @abstractmethod
    def getlightlevel(self):
        """Get int: Light Level"""
        pass

    @abstractmethod
    def turnon(self):
        """Turn this Light on"""
        pass

    @abstractmethod
    def turnoff(self):
        """Turn this Light off"""
        pass
