class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def set_time(self, hours, minutes, seconds):
        if hours > Time.max_hours:
            self.hours = "00"
        else:
            self.hours = hours
        if minutes > Time.max_minutes:
            self.hours += 1
            self.minutes = "00"
        else:
            self.minutes = minutes
        if seconds > Time.max_seconds:
            self.minutes += 1
            self.seconds = "00"
            if self.minutes > Time.max_minutes:
                self.hours += 1
                self.minutes = "00"
                if self.hours > Time.max_hours:
                    self.hours = "00"
        else:
            self.seconds = seconds

    def next_second(self):
        Time.set_time(self, self.hours, self.minutes, self.seconds + 1)
        return Time.get_time(self)
#
# time = Time(9, 30, 59)
# print(time.next_second())
# time = Time(10, 59, 59)
# print(time.next_second())
# time = Time(23, 59, 59)
# print(time.next_second())



