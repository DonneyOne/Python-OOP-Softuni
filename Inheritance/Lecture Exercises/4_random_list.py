from random import choice


class RandomList(list):
    def get_random_element(self):
        element = choice(self)
        self.remove(element)
        return element


ll = RandomList([1, 2, 3, 4, 5, 6])
print(ll.get_random_element())
