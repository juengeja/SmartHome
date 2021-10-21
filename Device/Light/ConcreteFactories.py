
from Device.Light.LEDStripe import LEDStripe, ModernLEDStripe
from Device.Light.LightChain import LightChain, ModernLightChain
from Device.Light.LightFactory import LightFactory
from Device.Light.Lightbulb import Lightbulb, ModernLightbulb
from Device.Light.StaircaseLight import StaircaseLight, ModernStaircaseLight


class StaircaseLightFactory(LightFactory):
    def create_light(self):
        return StaircaseLight()

    def create_modernlight(self):
        return ModernStaircaseLight()


class LEDStripeFactory(LightFactory):
    def create_light(self):
        return LEDStripe()

    def create_modernlight(self):
        return ModernLEDStripe()


class LightbulbFactory(LightFactory):
    def create_light(self):
        return Lightbulb()

    def create_modernlight(self):
        return ModernLightbulb()


class LightChainFactory(LightFactory):
    def create_light(self):
        return LightChain()

    def create_modernlight(self):
        return ModernLightChain()
