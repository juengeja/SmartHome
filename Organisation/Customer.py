class Customer:

    def __init__(self, name, email, phoneNumber):
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber

    def sign_up(self, name):
        print(name, "signed up")
