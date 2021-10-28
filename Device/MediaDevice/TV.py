from Device.MediaDevice.MediaDevice import MediaDevice


class TV(MediaDevice):

    def __init__(self, id, room, on, soundlevel, brightness):
        self.id = id
        self.room = room
        self.on = on
        self.soundlevel = soundlevel
        self.brightness = brightness

    def getroom(self):
        return self.room

    def setroom(self, room):
        self.room = room

    def pause(self):
        print("TV on pause")

    def play(self):
        print("TV on play")

    def forward(self):
        print("Fast forwarding TV")

    def backward(self):
        print("Fast backwarding TV")

    def start(self):
        self.on = True

    def shutdown(self):
        self.on = False

    def brighter(self):
        self.brightness += 1

    def darker(self):
        self.brightness -= 1
