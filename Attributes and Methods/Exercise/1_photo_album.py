class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = []
        for i in range(0, self.pages):
            self.photos.append([])
        self.page = 0

    @classmethod
    def from_photos_count(cls, photo_count):
        return PhotoAlbum(photo_count // 4)

    def add_photo(self, label):
        try:
            if len(self.photos[self.page]) != 4:
                self.photos[self.page].append(label)
                x = self.photos[self.page].index(label)
                return f"{label} photo added successfully on page {self.page+1} with slot {x+1}"
            elif len(self.photos[self.page]) == 4 and self.page < self.pages:
                self.page += 1
                self.photos[self.page].append(label)
                x = self.photos[self.page].index(label)
                return f"{label} photo added successfully on page {self.page+1} with slot {x+1}"

        except:
            return "No Free Slot"


    def display(self):
        result = ""
        for page in self.photos:
            result += "-"*11 + "\n"
            for photo in page:
                result += "[] "
            result += "\n"
        result += "-"*11 + "\n"
        return result

album = PhotoAlbum(1)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.photos)
print(album.display())
