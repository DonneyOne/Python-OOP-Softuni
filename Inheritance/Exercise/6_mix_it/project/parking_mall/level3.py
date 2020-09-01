from project.capacity_maxin import CapacityMixin
from project.parking_mall.parking_mall import ParkingMall

class Level3(ParkingMall, CapacityMixin):
    def __init__(self):
        ParkingMall.__init__(self, 80)