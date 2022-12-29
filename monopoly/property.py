class Property:
    def __init__(self, price, rent):
        self.price = price
        self.rent = rent
        self.owner = None

    def get_owner(self):
        return self.owner

    def set_owner(self, owner):
        self.owner = owner

    def get_rent(self):
        return self.rent

    def get_price(self):
        return self.price
