class Integer:
    def __init(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if not isinstance(value, float):
            return "Wrong type"
        return Integer(int(value))

    @classmethod
    def from_roman(cls, value):
        roman = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000,
                 'IV': 4,
                 'IX': 9,
                 'XL': 40,
                 'XC': 90,
                 'CD': 400,
                 'CM': 900}
        i = 0
        num = 0
        while i < len(value):
            if i + 1 < len(value) and value[i:i + 2] in roman:
                num += roman[value[i:i + 2]]
                i += 2
            else:
                num += roman[value[i]]
                i += 1
        return Integer(num)

    @classmethod
    def to_string(cls, value):
        if not isinstance(value, str):
            return "Wrong type"
        return Integer(int(value))

    def add(self, integer):
        if not isinstance(integer, Integer):
            return "Number should be integer"
        return self.value + integer.value

    def __str__(self):
        return f"{self.value}"
