from abc import ABC, abstractmethod


class LightFactory(ABC):
    @abstractmethod
    def create_light(self):
        pass

    @abstractmethod
    def create_modernlight(self):
        pass
