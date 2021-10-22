from Device.Light.LightInterfaces import Light, ModernLight


# Concrete Products
class Lightbulb(Light):
    """ Concrete Lightbulb Product. Implements Light Interface
        """
    def getproduct(self):
        """ prints: 'Lightbulb' string output
        """
        print("Lightbulb")


class ModernLightbulb(ModernLight):
    """ Concrete ModernLightbulb Product. Implements ModernLight Interface.
        """
    def getproduct(self) -> str:
        """ prints: 'Modern Lightbulb ON' string output
        """
        print("Modern Lightbulb ON")

    def getfeature(self) -> str:
        """ prints: 'Low Energy Notification' string output
        """
        print("Low Energy Notification")
