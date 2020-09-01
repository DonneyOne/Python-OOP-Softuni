class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    @staticmethod
    def customer_verification(example):
        return len(example) <= MovieWorld.customer_capacity()

    @staticmethod
    def dvd_verification(example):
        return len(example) <= MovieWorld.dvd_capacity()

    def add_customer(self, customer):
        if MovieWorld.customer_verification(self.customers):
            self.customers.append(customer)
        return "Capacity overloaded"

    def add_dvd(self, dvd):
        if MovieWorld.dvd_verification(self.dvds):
            self.dvds.append(dvd)
        return "Capacity overloaded"

    def rent_dvd(self, customer_id, dvd_id):
        customer = [customer for customer in self.customers if customer_id == customer.id][0]
        dvd = [dvd for dvd in self.dvds if dvd_id == dvd.id][0]
        if dvd.is_rented:
            return "DVD is already rented"
        elif dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        elif dvd.age_restriction > customer.age:
            return f"{customer.name} should be atleast {dvd.age_restriction} to rent this movie"
        else:
            customer.rented_dvds.append(dvd)
            dvd.is_rented = True
            return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = [customer for customer in self.customers if customer_id == customer.id][0]
        dvd = [dvd for dvd in self.dvds if dvd_id == dvd.id][0]
        if dvd in customer.rented_dvds and dvd.is_rented == True:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for i in self.customers:
            result += i.__repr__()
            result += "\n"
        for k in self.dvds:
            result += k.__repr__()
            result += "\n"
        return result
