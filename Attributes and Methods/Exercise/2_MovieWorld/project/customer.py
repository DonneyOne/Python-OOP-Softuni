class Customer:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    @staticmethod
    def rented_dvds_to_string(rented_dvds):
        return ', '.join(dvd.name for dvd in rented_dvds)

    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVDs" \
               f" ({self.rented_dvds_to_string(self.rented_dvds)})"
