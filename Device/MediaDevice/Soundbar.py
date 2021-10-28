from Device.MediaDevice.MediaDevice import MediaDevice


class SoundBar(MediaDevice):

    def __init__(self, id, room, on, soundlevel, songqueue):
        self.id = id
        self.room = room
        self.on = on
        self.soundlevel = soundlevel
        self.songqueue = songqueue

    def getroom(self):
        return self.room

    def setroom(self, room):
        self.room = room

    def pause(self):
        print("SoundBar on pause")

    def play(self):
        print("SoundBar on play")

    def forward(self):
        print("Fast forwarding SoundBar")

    def backward(self):
        print("Fast backwarding SoundBar")

    def start(self):
        self.on = True

    def shutdown(self):
        self.on = False
