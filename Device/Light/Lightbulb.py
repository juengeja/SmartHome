from Device.DeviceDecorator.LightDecorator import CountdownDecorator, SoundDecorator
from Device.Light.LightInterfaces import Light, ModernLight


class Lightbulb(Light):
    def getproduct(self):
        print("Lightbulb")


class ModernLightbulb(ModernLight):

    @CountdownDecorator
    def getproduct(self):
        print("Modern Lightbulb")

    def getfeature(self):
        print("Low Energy Consumption")
