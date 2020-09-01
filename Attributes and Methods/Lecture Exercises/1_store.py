class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def from_size(cls, name, type, size):
        return cls(name, type, size // 2)

    def can_add_item(self):
        return self.capacity > 0

    def add_item(self, item_name):
        if not self.can_add_item():
            return "Not enough capacity"
        self.capacity -= 1
        if item_name not in self.items():
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f"{item_name} added to the store"

    def can_remove(self, item_name, amount):
        return item_name in self.items and \
               amount <= self.items[item_name]

    def remove_item(self, item_name, amount):
        if not self.can_remove(item_name, amount):
            return f"Cannot remove {amount} of {item_name}"
        self.capacity += amount
        self.items[item_name] -= amount
        return f"{amount}{item_name} remove"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
