class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction " \
               f"{self.age_restriction}. Status: {self.is_rented_verification(self.is_rented)}"

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        x = date.split(".")
        month_num = x[1]
        month = DVD.month_string(int(month_num))
        year = x[2]
        return cls(name, id, year, month, age_restriction)

    @staticmethod
    def month_string(month_number):
        if month_number == 1:
            return "January"
        elif month_number == 2:
            return "February"
        elif month_number == 3:
            return "March"
        elif month_number == 4:
            return "April"
        elif month_number == 5:
            return "May"
        elif month_number == 6:
            return "June"
        elif month_number == 7:
            return "July"
        elif month_number == 8:
            return "August"
        elif month_number == 9:
            return "September"
        elif month_number == 10:
            return "October"
        elif month_number == 11:
            return "November"
        elif month_number == 12:
            return "December"

    @staticmethod
    def is_rented_verification(example):
        if example:
            return "rented"
        else:
            return "not rented"
