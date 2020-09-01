class Account:
    def __init__(self, id, balance, pin):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    @staticmethod
    def valid(pin, pin2):
        return pin == pin2

    def get_id(self, old_pin):
        if Account.valid(old_pin, self.__pin):
            return self.__id
        return "Wrong original pin"

    def change_pin(self, old_pin, new_pin):
        if Account.valid(old_pin, self.__pin):
            self.__pin = new_pin
            return "Pin changed"
        return f"Wrong original pin"
