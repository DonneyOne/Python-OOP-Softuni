class Hotel:
    def __init__(self, name):
        self.name = name
        self.guest = 0
        self.rooms = []

    @classmethod
    def from_stars(cls, stars_count):
        name = f"{stars_count} stars Hotel"
        return Hotel(name)

    def add_room(self, room):
        self.rooms.append(room)

    def get_room_by_room_number(self, room_number):
        return [room for room in self.rooms if room_number == room.number][0]

    def take_room(self, room_number, people):
        room = self.get_room_by_room_number(room_number)
        return room.take_room(people)

    def free_room(self, room_number):
        room = self.get_room_by_room_number(room_number)
        return room.free_room()
