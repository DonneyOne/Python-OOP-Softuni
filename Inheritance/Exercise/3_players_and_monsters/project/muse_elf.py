from elf import Elf


class Muse_Elf(Elf):
    def __init__(self, name, level):
        super().__init__(name, level)

    def __repr__(self):
        return f'{self.username} of type {__class__.__name__} has level {self.level}'

