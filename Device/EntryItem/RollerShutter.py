from Device.EntryItem.EntryItem import EntryItem


class RollerShutter(EntryItem):

    def __init__(self, id, room, locked, open):
        self.id = id
        self.room = room
        self.locked = locked
        self.open = open

    def getroom(self):
        """Get the room, in which the RollerShutter is located."""
        return self.room

    def setroom(self, room):
        """Set a room for this RollerShutter, in which it is located."""
        self.room = room

    def islocked(self):
        """Get boolean: Is the RollerShutter locked?"""
        return self.locked

    def isopen(self):
        """Get boolean: Is the RollerShutter open?"""
        return self.open

    def setlocked(self, locked):
        """Set boolean: Lock or unlock the RollerShutter"""
        self.locked = locked

    def setopen(self, open):
        """Set boolean: Open or close the RollerShutter"""
        self.open = open
