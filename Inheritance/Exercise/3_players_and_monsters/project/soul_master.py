from dark_wizard import Dark_Wizard


class Soul_Master(Dark_Wizard):
    def __init__(self, name, level):
        super().__init__(name, level)

    def __repr__(self):
        return f'{self.username} of type {__class__.__name__} has level {self.level}'
