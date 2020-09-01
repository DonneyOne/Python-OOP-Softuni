from dark_knight import Dark_Knight


class Blade_Knight(Dark_Knight):
    def __init__(self, name, level):
        super().__init__(name, level)

    def __repr__(self):
        return f'{self.username} of type {__class__.__name__} has level {self.level}'

