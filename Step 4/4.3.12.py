class Postman():
    def __init__(self):
        self.delivery = []

    def add_delivery(self, street, house, flat):
        self.delivery.append((street, house, flat))