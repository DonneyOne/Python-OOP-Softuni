class Technology:
    def __init__(self, memory, memory_taken):
        self.memory = memory
        self.memory_taken = memory_taken

    @staticmethod
    def memory_validator(memory, memory_needed):
        return memory >= memory_needed
