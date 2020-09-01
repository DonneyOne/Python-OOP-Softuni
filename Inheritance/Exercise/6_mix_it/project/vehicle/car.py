from vehicle import Vehicle
from project.capacity_maxin import CapacityMixin


class Car(Vehicle, CapacityMixin):
    def __init__(self, available_seats, fuel_tank, fuel_consumption, fuel):
        super().__init__(available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self.__fuel = fuel

    @staticmethod
    def fuel_validator(fuel, capacity):
        return fuel >= capacity

    @staticmethod
    def fuel_consumption_on_distance(consumption, distance):
        return distance * consumption

    @staticmethod
    def needed_fuel_validator(needed_fuel, fuel):
        return fuel >= needed_fuel

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel_setter(self, value):
        if Car.fuel_validator(value, self.fuel_tank):
            self.__fuel = value
        else:
            return "The fuel tank cannot fit this amount"

    @staticmethod
    def mixin_validator(example):
        return isinstance(example, str)

    def drive(self, distance):
        needed_fuel = Car.fuel_consumption_on_distance(self.fuel_consumption, distance)
        if Car.needed_fuel_validator(needed_fuel, self.__fuel):
            self.__fuel -= needed_fuel
            return "We've enjoyed the travel!"
        return "Not enough fuel!"

    def refuel(self, liters):
        available_liters = CapacityMixin.get_capacity(self.fuel_tank, liters)
        if CapacityMixin.mixin_validator(available_liters):
            return available_liters
        else:
            if self.__fuel + liters <= self.fuel_tank:
                self.__fuel += liters
                return self.fuel_tank - self.__fuel
            return "Not enough capacity in the fuel tank"
