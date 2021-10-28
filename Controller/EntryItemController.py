from Controller.Controller import Controller


class EntryItemController(Controller):

    def turnon(self):
        pass

    def turnoff(self):
        pass

    def __init__(self, windows, doors, rollershutters):
        self.windows = windows
        self.doors = doors
        self.rollershutters = rollershutters

    def openall(self, room):
        pass

    def closeall(self, room):
        pass

    def open(self, id):
        pass

    def close(self, id):
        pass
