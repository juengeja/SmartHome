import minibar as minibar

from Device.DeviceDecorator.FridgeDecorator import AddItemsDecorator
from Device.DeviceDecorator.LightDecorator import CountdownDecorator, SoundDecorator
from Device.Fridge.BeverageCooler import BeverageCooler
from Device.Fridge.FridgeChain import FridgeChain
from Device.Fridge.FridgeHandler import FridgeHandler
from Device.Fridge.KitchenFridge import KitchenFridge
from Device.Fridge.Minibar import Minibar
from Device.Light import LightbulbFactory

if __name__ == '__main__':
    # lightbulb = LightbulbFactory().create_modernlight()
    # countdownDecorator = CountdownDecorator(lightbulb)
    # soundDecoractor = SoundDecorator(lightbulb)
    # lightbulb.getproduct()
    # soundDecoractor.getproduct()
    # countdownDecorator.getfeature()
    # run_singleModernLightExample()

    fridgeChain = FridgeChain()
    addItemsDecorator = AddItemsDecorator(fridgeChain.link1, fridgeChain)
    addItemsDecorator.get_item("cola", 2)

    addItemsDecorator = AddItemsDecorator(fridgeChain.link3, fridgeChain)
    addItemsDecorator.add_item("water", 2)
