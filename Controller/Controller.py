from abc import abstractmethod


class Controller():

    @abstractmethod
    def turnoff(self):
        pass

    @abstractmethod
    def turnon(self):
        pass
