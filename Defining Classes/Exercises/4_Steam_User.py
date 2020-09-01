class SteamUser:
    played_hours = 0

    def __init__(self, username, games):
        self.username = username
        self.games = games

    def play(self, game, hours):
        if game in self.games:
            SteamUser.played_hours += hours
            return f"{self.username} is playing {game}"
        else:
            return f"{game} is not in the library"

    def buy_game(self, game):
        if game not in self.games:
            self.games.append(game)
            return f"{self.username} bought {game}"

        else:
            return f"{game} already in the library"

    def stats(self):
        games_count = 0
        for i in self.games:
            games_count += 1
        return f"{self.username} has {games_count} games. Total play time: {SteamUser.played_hours}"


user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.played_hours)
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.stats())
# Peter is playing Fortnite
# Oxygen Not Included not in library
# CS:GO is already in your library
# Peter bought Oxygen Not Included
# Peter is playing Oxygen Not Included
# Peter has 4 games. Total play time: 9
