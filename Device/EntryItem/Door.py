from Device.EntryItem.EntryItem import EntryItem


class Door(EntryItem):

    def __init__(self, id, room, locked, open):
        self.id = id
        self.room = room
        self.locked = locked
        self.open = open

    def getroom(self):
        """Get the room, in which the door is located."""
        return self.room

    def setroom(self, room):
        """Set a room for this door, in which it is located."""
        self.room = room

    def islocked(self):
        """Get boolean: Is the door locked?"""
        return self.locked

    def isopen(self):
        """Get boolean: Is the door open?"""
        return self.open

    def setlocked(self, locked):
        """Set boolean: Lock or unlock the door"""
        self.locked = locked

    def setopen(self, open):
        """Set boolean: Open or close the door"""
        self.open = open
