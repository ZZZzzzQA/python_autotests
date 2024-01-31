#тест API pokemonbattle

import requests
token = "7e7432b6573a18615f82cd9bb9b9ea9d"

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': token}

body = {
    "name": "Бульбаш",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
#создание покемона
response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=15)
print(f'Сатус код {response.status_code}.Сообщение:{response.json()["message"]}')
response_json = response.json()
key_id_pokemon = response_json["id"]
"""body3 = {
    "pokemon_id": "29181"
}
#kill покемона
response = requests.post(url=f'{URL}/pokemons/knockout', json=body3, headers=HEADER, timeout=10)"""

body2 = {
    "pokemon_id": key_id_pokemon,
    "name": "Бандерлог",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
#изменение имени покемона
response = requests.put(url=f'{URL}/pokemons', json=body2, headers=HEADER, timeout=10)
print(f'Сатус код {response.status_code}.Сообщение:{response.text}')


body4 = {
    "pokemon_id": key_id_pokemon
}
#поймать в покебол покемона
response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body4, headers=HEADER, timeout=10)
print(f'Сатус код {response.status_code}.Сообщение:{response.text}')





