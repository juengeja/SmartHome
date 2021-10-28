from Device.Sensor.SecuritySensor import SecuritySensor


class IRMotionSensor(SecuritySensor):

    def __init__(self, id, room, active):
        self.id = id
        self.room = room
        self.active = active
        self.alarm = False
        self.motiondetected = False

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

    def isalarm(self):
        return self.alarm

    def triggeralarm(self):
        if self.alarm == True:
            self.alarm = False
        else:
            self.alarm = True

    def ismotiondetected(self):
        return self.motiondetected
