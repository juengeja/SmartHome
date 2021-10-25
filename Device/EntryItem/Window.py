from Device.EntryItem.EntryItem import EntryItem


class Window(EntryItem):

    def __init__(self, id, room, locked, open, position):
        self.id = id
        self.room = room
        self.locked = locked
        self.open = open
        self.position = position

    def getroom(self):
        """Get the room, in which the window is located."""
        return self.room

    def setroom(self, room):
        """Set a room for this window, in which it is located."""
        self.room = room

    def islocked(self):
        """Get boolean: Is the window locked?"""
        return self.locked

    def isopen(self):
        """Get boolean: Is the window open?"""
        return self.open

    def setlocked(self, locked):
        """Set boolean: Lock or unlock the window"""
        self.locked = locked

    def setopen(self, open):
        """Set boolean: Open or close the window"""
        self.open = open

    def getposition(self):
        """Get the current position of the window: is it completely open,
        tilted, ..."""
        return self.position

    def setposition(self, position):
        """Set the position of the window: String"""
        self.position = position