class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION

    @staticmethod
    def fuel_consuption_return(fuel_consuption, kilometres):
        return fuel_consuption*kilometres

    @staticmethod
    def validator_fuel_needed(fuel, needed_fuel):
        return fuel >= needed_fuel

    def drive(self, kilometres):
        needed_fuel = Vehicle.fuel_consuption_return(self.fuel_consumption, kilometres)
        if Vehicle.validator_fuel_needed(self.fuel, needed_fuel):
            self.fuel -= needed_fuel
            return "Driving.."
        return "Not enough fuel"

