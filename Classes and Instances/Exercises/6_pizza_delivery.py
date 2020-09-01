class PizzaDelivery:
    ordered = False

    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient, quantity, ingredient_price):
        if not PizzaDelivery.ordered:
            if ingredient in self.ingredients:
                self.ingredients[ingredient] += quantity
                self.price = self.price + (ingredient_price * quantity)
            else:
                self.ingredients[ingredient] = quantity
                self.price = self.price + (ingredient_price * quantity)
        else:
            return f"Pizza {self.name} already prepared and we can't make any changes!"

    def remove_ingredient(self, ingredient, quantity, ingredient_price):
        if not PizzaDelivery.ordered:
            if ingredient not in self.ingredients:
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
            elif ingredient in self.ingredients and quantity > self.ingredients[ingredient]:
                return f"Please check again the desired quantity of {ingredient}"
            else:
                if self.ingredients[ingredient] - quantity == 0:
                    self.price = self.price - (quantity * ingredient_price)
                    del self.ingredients[ingredient]
                else:
                    self.ingredients[ingredient] -= quantity
                    self.price = self.price - (quantity * ingredient_price)
        else:
            return f"Pizza {self.name} already prepared and we can't make any changes!"

    def pizza_ordered(self):
        PizzaDelivery.ordered = True
        str_print = ""
        for k,v in self.ingredients.items():
            str_print += k
            str_print += " : "
            x = f"{v}"
            str_print += x
            str_print += ", "
        return f"You've ordered pizza {self.name} prepared with " \
               f"{str_print} and the price will be {self.price}lv."
#
# Margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
# Margarita.add_extra('mozzarella', 1, 0.5)
# Margarita.add_extra('cheese', 1, 1)
# Margarita.remove_ingredient('cheese', 1, 1)
# print(Margarita.remove_ingredient('bacon', 1, 2.5))
# print(Margarita.remove_ingredient('tomatoes', 2, 0.5))
# Margarita.remove_ingredient('cheese', 2, 1)
# Margarita.remove_ingredient('cheese', 2, 1)
# print(Margarita.pizza_ordered())
# print(Margarita.add_extra('cheese', 1, 1))

