from Device.Sensor.Sensor import Sensor


class TemparatureSensor(Sensor):

    def __init__(self, id, room, active):
        self.id = id
        self.room = room
        self.active = active
        self.temparature = 5

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

    def gettemparature(self):
        self.temparature += 1
        return self.temparature