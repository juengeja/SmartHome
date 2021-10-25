from abc import abstractmethod
from Device.Device import Device


class MediaDevice(Device):

    @abstractmethod
    def pause(self):
        """Set the MediaDevice to pause"""
        pass

    @abstractmethod
    def play(self):
        """Set MediaDevice to play"""
        pass

    @abstractmethod
    def forward(self):
        """Spool forward"""
        pass

    @abstractmethod
    def backward(self):
        """Spool backward"""
        pass

    @abstractmethod
    def start(self):
        """Start the MediaDevice"""
        pass

    @abstractmethod
    def shutdown(self):
        """Shut the MediaDevice down"""
        pass
