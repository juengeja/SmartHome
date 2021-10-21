
from Device.Light.LightInterfaces import Light, ModernLight


class Lightbulb(Light):
    def getproduct(self):
        print("Lightbulb")


class ModernLightbulb(ModernLight):

    def getproduct(self) -> str:
        print ("Modern Lightbulb")

    def getfeature(self) -> str:
        print ("Low Energy Consumption")
