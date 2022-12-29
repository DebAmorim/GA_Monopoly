class Player:
    def __init__(self, id, position, money, bankrupt, behavior):
        self.id = id
        self.position = None
        self.money = money
        self.bankrupt = False
        self.behavior = behavior

    def get_id(self):
        return self.id
    
    def get_money(self):
        return self.money

    def get_behavior(self):
        return self.behavior

    def is_bankrupt(self):
        return self.bankrupt

    def set_bankrupt(self, bankrupt):
        self.bankrupt = bankrupt

    def get_position(self):
        return self.position

    def pay(self, value):
        payment = value
        if self.money < value:
            payment = self.money
        
        self.money -= value
        return payment

    def receive(self, value):
        self.money += value
    
    def move(self, steps):
        if self.position == None:
            self.position = steps -1
        self.position += steps
        if self.position > 27:
            self.position -= 28
        return True
