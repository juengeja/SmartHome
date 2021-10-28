from Device.Sensor.Sensor import Sensor


class MoisturisationSensor(Sensor):

    def __init__(self, id, room, active):
        self.id = id
        self.room = room
        self.active = active
        self.moist = 98

    def getroom(self):
        return self.room

    def setroom(self, room):
        self.room = room

    def isactive(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def getmoist(self):
        self.moist += 1
        return self.moist
