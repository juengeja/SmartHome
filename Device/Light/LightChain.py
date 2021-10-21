from Device.Light.LightInterfaces import Light, ModernLight


class LightChain(Light):
    def getproduct(self):
        print("LightChain")


class ModernLightChain(ModernLight):
    def getproduct(self):
        print("Modern LightChain")

    def getfeature(self):
        print("Blink Effect")
