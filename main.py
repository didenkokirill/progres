import requests

url = 'https://pokeapi.co/api/v2/'

class BasePokemon:
    def __init__(self, name):
        self.name = name
    def visual(self):
        print(self)


class Pokemon(BasePokemon):
    def __init__(self, id, name, height, weight):
        self.id = id  # ID
        self.name = name  # Имя
        self.height = height  # Рост
        self.weight = weight  # Вес


class PokeAPI:
    global url
    def get_pokemon(name_id):
        newurl = url + str(name_id)
        print(newurl)
        res = requests.get(newurl).json()
        return Pokemon(res['id'], res['name'], res['height'], res['weight'])
a = PokeAPI.get_pokemon(1)
print(a.visual())