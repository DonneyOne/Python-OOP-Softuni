from player import Player
from typing import List


class Guild:

    def __init__(self, name):
        self.name = name
        self.list_of_players: List[Player] = []

    def assign_player(self, new_player: Player):
        new_player.guild = self.name
        self.list_of_players.append(new_player)
        return f"Welcome player {new_player.name} to the guild {self.name}."

    def kick_player(self, player_name: str):
        player_to_delete = [player_delete for player_delete in self.list_of_players if player_delete.name == player_name]
        if player_to_delete:
            self.list_of_players.remove(player_to_delete[0])
            player_to_delete[0].guild = "Unaffiliated"



    def guild_info(self):
        x = [player.player_info() for player in self.list_of_players]
        str = ""
        for y in x:
            str+=y
        return f"Guild: {self.name} \n" \
               f"{str}"

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())


