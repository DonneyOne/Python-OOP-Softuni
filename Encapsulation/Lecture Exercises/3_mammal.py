class Mammal:
    __kingdom = "animals"

    def __init__(self, name, sound, type):
        self.name = name
        self.sound = sound
        self.type = type

    def make_sound(self):
        return f"{self.name} makes sound {self.sound}"

    def get_kingdom(self):
        return Mammal.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"
