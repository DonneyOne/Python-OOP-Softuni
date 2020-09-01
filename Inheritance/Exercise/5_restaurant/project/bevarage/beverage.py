from project.product import Product


class Beverage(Product):
    def __init__(self, name, price, millilitres):
        super().__init__(name, price)
        self.__millilitres = millilitres

    @property
    def millilitres(self):
        return self.__millilitres
