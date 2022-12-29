class Behavior:
    def __init__(self) -> None:
        pass

    def decide(self):
        return True

class Demanding(Behavior):
    def __init__(self):
        pass
    
    def decide(self, money, rent, price):
        if money < price:
            return False
        
        return rent>22


from random import choice
class Random(Behavior):
    def __init__(self):
        pass
    
    def decide(self, money, rent, price):
        if money < price:
            return False
        
        return choice()

class Cautious(Behavior):
    def __init__(self):
        pass
    
    def decide(self, money, rent, price):
        return money-price >= 500

class Impulsive(Behavior):
    def __init__(self):
        pass

    def decide(self, money, rent, price):
        return money - price >= 0