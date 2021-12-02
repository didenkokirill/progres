import requests

url = 'https://pokeapi.co/api/v2/pokemon/'


class BasePokemon:
    def __init__(self, name):
        self.name = name
    def visual(self):
        pass


class Pokemon(BasePokemon):
    def __init__(self, id, name, height, weight):
        self.id = id  # ID
        self.name = name  # Имя
        self.height = height  # Рост
        self.weight = weight  # Вес

    global name

    def __getitem__(self, item):
        return name


class PokeAPI:
    global url

    def get_pokemon(name_id):
        newurl = url + str(name_id)
        res = requests.get(newurl).json()
        return Pokemon(res['id'], res['name'], res['height'], res['weight'])
    def get_all(get_full=False):
        i = 1
        if get_full == True:
            while True:
                yield PokeAPI.get_pokemon(i)
                i += 1
        elif get_full == False:
            while True:
                a = PokeAPI.get_pokemon(i)
                yield a['name']
                i += 1

for i in range(50):
    print(PokeAPI.get_all(True))

