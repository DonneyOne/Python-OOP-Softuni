class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = True

    def install(self, app, app_memory):

        if self.memory > app_memory and not self.is_on:
            return "The Phone is not powered on"
        elif self.memory < app_memory:
            return "Not enough memory"
        self.apps.append(app)
        self.memory -= app_memory
        return f"Installing {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}"

