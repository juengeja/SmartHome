
from time import sleep


from Device.Light.LightInterfaces import ModernLight


class ModernLightDecorator(ModernLight):
    _modernlight: ModernLight = None

    def __init__(self, modernlight: ModernLight) -> None:
        self._modernlight = modernlight

    @property
    def modernLight(self) -> str:
        return self._modernlight

    def getproduct(self) -> str:
        return self._modernlight.getproduct()

    def getfeature(self) -> str:
        return self._modernlight.getfeature()


class CountdownDecorator(ModernLightDecorator):

    def getfeature(self) -> str:
        count = 5
        for x in range(count, -1, -1):
            print("battery:", x)
            sleep(1)
        return self.modernLight.getfeature()


class SoundDecorator(ModernLightDecorator):

    def getproduct(self) -> str:
        print("Soothing music starts")
        return self.modernLight.getproduct()
