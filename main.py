from Device.DeviceDecorator2.LightDecorator import CountdownDecorator, SoundDecorator
from Device.Light import LightbulbFactory

if __name__ == '__main__':
    lightbulb = LightbulbFactory().create_modernlight()
    countdownDecorator = CountdownDecorator(lightbulb)
    soundDecoractor = SoundDecorator(lightbulb)
    # lightbulb.getproduct()
    soundDecoractor.getproduct()
    countdownDecorator.getfeature()
    # run_singleModernLightExample()
