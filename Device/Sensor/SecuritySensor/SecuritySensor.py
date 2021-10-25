from abc import abstractmethod
from Device.Sensor.Sensor import Sensor


class SecuritySensor(Sensor):

    @abstractmethod
    def isalarm(self):
        pass

    @abstractmethod
    def triggeralarm(self):
        pass
