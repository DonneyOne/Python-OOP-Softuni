from song import Song
from album import Album


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        album_in_list = [element for element in self.albums if element.name == album_name]
        if album_in_list[0].published:
            return "Album has been published. It cannot be removed."
        if album_in_list:
            self.albums.remove(album_in_list[0])
            return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        str = f"Band {self.name} \n"
        for k in self.albums:
            str += k.details()
        return str


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
