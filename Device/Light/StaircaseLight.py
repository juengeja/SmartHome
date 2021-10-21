from Device.Light.LightInterfaces import ModernLight, Light


class StaircaseLight(Light):
    def getproduct(self):
        print("StaircaseLight")


class ModernStaircaseLight(ModernLight):
    def getproduct(self):
        print("Modern StaircaseLight")

    def getfeature(self):
        print("Dimmable")
