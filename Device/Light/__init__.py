# Run Methods
from self import self

from Device.Light.ConcreteFactories import LightbulbFactory, StaircaseLightFactory, LightChainFactory, LEDStripeFactory


def run_singleModernLightExample():
    light_a = LightbulbFactory().create_modernlight()
    light_a.getproduct()
    light_a.getfeature()


def run_lightExample():
    for factorya in (StaircaseLightFactory(), LightbulbFactory(), LEDStripeFactory()):
        light_b = factorya.create_light()
        light_b.getproduct()


def run_modernlightExample():
    for factoryb in (LightChainFactory(), LightbulbFactory(), LEDStripeFactory()):
        light_c = factoryb.create_modernlight()
        light_c.getproduct()
        light_c.getfeature()
