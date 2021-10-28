from Controller.Controller import Controller


class LightsController(Controller):

    def turnon(self):
        pass

    def turnoff(self):
        pass

    def __init__(self, windows, doors, rollershutters):
        self.windows = windows
        self.doors = doors
        self.rollershutters = rollershutters

    def turnalloff(self, room):
        pass

    def turnallon(self, room):
        pass

    def turnoff(self, id):
        pass

    def turnon(self, id):
        pass
