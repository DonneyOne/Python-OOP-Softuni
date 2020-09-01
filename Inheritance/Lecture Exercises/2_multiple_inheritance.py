class Person:
    def sleep(self):
        return "Sleeping.."

class Employee:
    def get_fired(self):
        return "Fired.."

class Teacher(Person, Employee):
    def teaching(self):
        return "Teaching"

print(Teacher().sleep())