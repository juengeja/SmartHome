from abc import abstractmethod
from Device.Device import Device


class Sensor(Device):

    @abstractmethod
    def isactive(self):
        pass

    @abstractmethod
    def activate(self):
        pass

    @abstractmethod
    def deactivate(self):
        pass
