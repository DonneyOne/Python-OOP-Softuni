from project.bevarage.beverage import Beverage


class ColdBeverage(Beverage):
    def __init__(self, name, price, millilitres):
        super().__init__(name, price, millilitres)
