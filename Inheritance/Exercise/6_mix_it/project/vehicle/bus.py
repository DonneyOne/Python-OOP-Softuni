from project.capacity_maxin import CapacityMixin
from vehicle import Vehicle


class Bus(CapacityMixin, Vehicle):

    def __init__(self, available_seats, ticket_price):
        Vehicle.__init__(available_seats)
        self.ticket_price = ticket_price
        self.ticket_sold = 0

    def get_ticket(self, tickets_count):
        tickets_available = CapacityMixin.get_capacity(self.available_seats, tickets_count)
        if not CapacityMixin.mixin_validator(tickets_available):
            self.available_seats -= tickets_count
            self.ticket_sold += tickets_count
            return "Ticket bought!"
        return tickets_available

    def get_total_profit(self):
        return self.ticket_sold * self.ticket_price
