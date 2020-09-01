from project.capacity_maxin import CapacityMixin

class ParkingMall(CapacityMixin):
    def __init__(self, parking_lots):
        self.parking_lots = parking_lots

    def check_availability(self):
        pass
