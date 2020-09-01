from typing import List
from pokemon import Pokemon
class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon : List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon):
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        da = [poke for poke in self.pokemon if poke.name == pokemon_name]
        if da:
            self.pokemon.remove(da[0])
            return f"You have released {da[0].name}"

    def trainer_data(self):
        str = ""
        str += f"Pokemon trainer {self.name} \n"
        str += f"Pokemon count {len(self.pokemon)} \n"
        Tokens = [x.pokemon_details() for x in self.pokemon]
        if Tokens:
            for k in Tokens:
                str += f"- {k} \n"
        return str



# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())

