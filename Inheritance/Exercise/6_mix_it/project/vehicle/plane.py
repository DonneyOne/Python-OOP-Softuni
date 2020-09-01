from project.capacity_maxin import CapacityMixin
from vehicle import Vehicle


class Plane(CapacityMixin, Vehicle):

    @staticmethod
    def row_validator(row_number, rows):
        return row_number > rows

    def __init__(self, available_seats, rows, seats_per_row):
        Vehicle.__init__(self, available_seats)
        self.rows = rows
        self.seats_per_row = seats_per_row

    def buy_tickets(self, row_number, tickets_count):
        seats_for_sell = CapacityMixin.get_capacity(self.seats_per_row, tickets_count)
        if Plane.row_validator(row_number, self.rows):
            return f"There is no row {row_number} in the plane"
        elif CapacityMixin.mixin_validator(seats_for_sell):
            return f"Not enough tickets on row {row_number}!"
        else:
            self.available_seats -= tickets_count
            return tickets_count



