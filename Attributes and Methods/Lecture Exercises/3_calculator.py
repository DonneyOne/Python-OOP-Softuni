class Calculator:
    @staticmethod
    def multiply(*args):
        result = 1
        for i in args:
            result *= i

        return result

    @staticmethod
    def add(*args):
        result = 0
        for i in args:
            result += i

        return result

    @staticmethod
    def devide(*args):
        result = args[0]
        for i in args[1:]:
            result /= i

        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for i in args[1:]:
            result -= i

        return result
