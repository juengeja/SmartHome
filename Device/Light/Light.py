from abc import abstractmethod
from Device.Device import Device


class Light(Device):

    @abstractmethod
    def getlightlevel(self):
        pass

    @abstractmethod
    def turnon(self):
        pass

    @abstractmethod
    def turnoff(self):
        pass
