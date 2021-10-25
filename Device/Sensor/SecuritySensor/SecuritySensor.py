from abc import abstractmethod
from Device.Sensor.Sensor import Sensor


class SecuritySensor(Sensor):

    @abstractmethod
    def isalarm(self):
        """Get boolean: Is an alarm triggered?"""
        pass

    @abstractmethod
    def triggeralarm(self):
        """Set boolean: Trigger an alarm"""
        pass
