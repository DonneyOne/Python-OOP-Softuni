class CapacityMixin:
    @staticmethod
    def get_capacity(capacity, amount):
        if amount > capacity:
            return "Capacity reached!"
        return capacity - amount

    @staticmethod
    def mixin_validator(example):
        return isinstance(example, str)
