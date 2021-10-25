from abc import abstractmethod
from Device.Device import Device


class Sensor(Device):

    @abstractmethod
    def isactive(self):
        """Get boolean: Is the Sensor active?"""
        pass

    @abstractmethod
    def activate(self):
        """Set boolean to 'true': Activate the Sensor"""
        pass

    @abstractmethod
    def deactivate(self):
        """Set boolean to 'false': Deactivate Sensor"""
        pass
