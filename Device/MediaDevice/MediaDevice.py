from abc import abstractmethod
from Device.Device import Device


class MediaDevice(Device):

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def forward(self):
        pass

    @abstractmethod
    def backward(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass
    