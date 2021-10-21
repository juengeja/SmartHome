from Device.Light.LightInterfaces import Light, ModernLight


class LEDStripe(Light):
    def getproduct(self):
        print("LEDStripe")


class ModernLEDStripe(ModernLight):
    def getproduct(self):
        print("Modern LEDStripe")

    def getfeature(self):
        print("Connectable")
