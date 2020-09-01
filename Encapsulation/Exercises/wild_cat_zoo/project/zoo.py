class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.list_animals = []
        self.workers = []
        self.__animal_capacity = animal_capacity
        self.__budget = budget
        self.__workers_capacity = workers_capacity

    def __animal_validator(self, price_validator: int):
        return self.__animal_capacity > len(self.list_animals) and self.__budget >= price_validator

    def __workers_validator(self):
        return self.__workers_capacity > len(self.workers)

    def __worker_with_name(self, worker_name):
        return [worker_instance for worker_instance in self.workers if worker_name == worker_instance.name][0]

    @staticmethod
    def filter(list_filter, name):
        return [a for a in list_filter if a.__class__.__name__ == name]

    def salaries_budget(self):
        salaries_budget = 0
        for k in self.workers:
            salaries_budget += k.salary
        return salaries_budget

    def tending_budget(self):
        tending_budget = 0
        for k in self.list_animals:
            tending_budget += k.get_needs()
        return tending_budget

    def add_animal(self, animal, price_animal):
        if self.__animal_validator(price_animal):
            self.list_animals.append(animal)
            self.__budget -= price_animal
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price_animal:
            return 'Not enough budget'
        else:
            return 'Not enough space for the animal'

    def hire_worker(self, worker):
        if self.__workers_validator():
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker_instance = self.__worker_with_name(worker_name)
        if worker_instance in self.workers:
            self.workers.remove(worker_instance)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salaries = self.salaries_budget()
        if self.__budget >= sum_salaries:
            self.__budget -= sum_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tending_budget = self.tending_budget()
        if self.__budget >= tending_budget:
            self.__budget -= tending_budget
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = Zoo.filter(self.list_animals, "Lion")
        tigers = Zoo.filter(self.list_animals, "Tiger")
        cheetahs = Zoo.filter(self.list_animals, "Cheetah")
        lions_string = ""
        tigers_string = ""
        cheetahs_string = ""
        for lion in lions:
            lions_string += lion.__repr__() + "\n"
        for cheetah in cheetahs:
            cheetahs_string += cheetah.__repr__() + "\n"
        for tiger in tigers:
            tigers_string += tiger.__repr__() + "\n"
        return f"You have {len(self.list_animals)} animals\n" \
               f"----- {len(lions)} Lions:\n" \
               f"{lions_string}\n" \
               f"----- {len(tigers)} Tigers:\n" \
               f"{tigers_string}\n" \
               f"----- {len(cheetahs)} Cheetahs:\n" \
               f"{cheetahs_string}"

    def workers_status(self):
        keepers = Zoo.filter(self.workers, "Keeper")
        caretakers = Zoo.filter(self.workers, "Caretaker")
        vets = Zoo.filter(self.workers, "Vet")
        keepers_string = ""
        caretakers_string = ""
        vets_string = ""
        for keeper in keepers:
            keepers_string += keeper.__repr__() + "\n"
        for caretaker in caretakers:
            caretakers_string += caretaker.__repr__() + "\n"
        for vet in vets:
            vets_string += vet.__repr__() + "\n"

        return f"You have {len(self.workers)} workers \n" \
               f"----- {len(keepers)} Keepers: \n" \
               f"{keepers_string}\n" \
               f"----- {len(caretakers)} Caretakers:\n" \
               f"{caretakers_string}\n" \
               f"----- {len(vets)} Vets:\n" \
               f"{vets_string}"
