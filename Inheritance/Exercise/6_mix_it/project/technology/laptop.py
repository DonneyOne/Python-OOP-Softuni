from project.technology.technology import Technology
from project.capacity_maxin import CapacityMixin


class Laptop(Technology, CapacityMixin):
    def __init__(self, memory, memory_taken):
        Technology.__init__(self, memory, memory_taken)
        self.available_memory = self.memory - self.memory_taken

    def install_software(self, software, software_memory):
        if Technology.memory_validator(self.available_memory, software_memory):
            return CapacityMixin.get_capacity(self.available_memory, software_memory)
        return f"You don't have enough space for {software}!"
