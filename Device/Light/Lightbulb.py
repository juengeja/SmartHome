from Device.Light.LightInterfaces import Light, ModernLight


# Concrete Products
class Lightbulb(Light):
    def getproduct(self):
        print("Lightbulb")


class ModernLightbulb(ModernLight):

    def getproduct(self) -> str:
        print("Modern Lightbulb ON")

    def getfeature(self) -> str:
        print("Low Energy Notification")
