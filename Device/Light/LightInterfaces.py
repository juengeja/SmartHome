from abc import ABC, abstractmethod


class Light(ABC):
    @abstractmethod
    def getproduct(self):
        pass


class ModernLight(ABC):
    @abstractmethod
    def getproduct(self):
        pass

    @abstractmethod
    def getfeature(self):
        pass
