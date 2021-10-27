from abc import abstractmethod


class Controller():

    @abstractmethod
    def turnoff(self):
        """Turn Devices off"""
        pass

    @abstractmethod
    def turnon(self):
        """Turn Devices on"""
        pass
