class Animal:
    def __init__(self, name):
        self.__name = name

    @property
    def get_name(self):
        return self.__name
