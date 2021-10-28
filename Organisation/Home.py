class Home:

    def __init__(self, id, name, address, status):
        self.id = id
        self.name = name
        self.address = address
        self.status = status

    def __getstate__(self):
        return self.status

    def close_all(self):
        print("Closing everything")

        print("Everything closed")
