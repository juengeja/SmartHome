from abc import ABC
from time import sleep
from types import MethodType


class LightDecorator(ABC):
    def __get__(self, instance, cls):
        # Return a Method if it is called on an instance
        return self if instance is None else MethodType(self, instance)


class CountdownDecorator(LightDecorator):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        count = 5
        for x in range(count, -1, -1):
            print("timer:", x)
            sleep(1)
        print("Light ON:")
        return self.func(*args, **kwargs)


class SoundDecorator(LightDecorator):

    @CountdownDecorator
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Soothing music starts")
        return self.func(*args, **kwargs)
