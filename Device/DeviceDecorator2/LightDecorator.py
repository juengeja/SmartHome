from abc import ABC
from time import sleep
from Device.Light.LightInterfaces import ModernLight


# Abstract Base Decorator
class ModernLightDecorator(ModernLight, ABC):
    """Abstract class to all decorators complementing ModernLight Products
        Parameters:
                ModernLight object to be decorated
        Attributes:
            _modernlight : ModernLight
                represents the passed ModernLight object
        Methods:
            modernLight()
                returns the ModernLight product setter and getters
            getproduct()
                returns the getproduct() method of the passed ModernLight object
            getfeature()
                returns the getfeature() method of the passed ModernLight object
    """
    _modernlight: ModernLight

    def __init__(self, modernlight: ModernLight):
        self._modernlight = modernlight

    @property
    def modernLight(self) -> str:
        return self._modernlight

    def getproduct(self) -> str:
        return self._modernlight.getproduct()

    def getfeature(self) -> str:
        return self._modernlight.getfeature()


# Lightweight Decorators
class CountdownDecorator(ModernLightDecorator):
    """Extends the Abstract ModernLightDecorator class.
    """

    def getfeature(self) -> str:
        """ Overwrites the Abstract ModernLightDecorator getfeature() Method. Provides additional short 5 second
        counter + 'battery' string output Returns: getfeature() method of passed ModernLight Object
        """
        count = 5
        for x in range(count, -1, -1):
            print("battery:", x)
            sleep(1)
        return self.modernLight.getfeature()


class SoundDecorator(ModernLightDecorator):
    """Extends the Abstract ModernLightDecorator class.
    """

    def getproduct(self) -> str:
        """ Overwrites the Abstract ModernLightDecorator getproduct() Method. Provides additional 'Soothing music
        starts' string output Returns: getfeature() method of passed ModernLight Object
        """
        print("Soothing music starts")
        return self.modernLight.getproduct()
