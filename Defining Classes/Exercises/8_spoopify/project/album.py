from song import Song


class Album:

    def __init__(self, name, songs):
        self.name = name
        if not isinstance(songs, list):
            self.songs = [songs]
        else:
            self.songs = songs
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. Its a single!"
        elif self.published:
            return "Cannot add songs. Album is published"
        elif song in self.songs:
            return "Song is already in album"
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name} "

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        song_in_list = [element for element in self.songs if element.name == song_name]
        if not song_in_list:
            return "Song is not in the album."
        self.songs.remove(song_in_list[0])
        return f"Removed song {song_in_list[0].name} from album {self.name}"

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        string_lol = f"Album: {self.name} \n"
        for k in self.songs:
            string_lol += "== " + k.get_info() + "\n"
        return string_lol

