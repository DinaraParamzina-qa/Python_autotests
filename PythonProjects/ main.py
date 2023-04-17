import requests

token = 'здесь токен'
base_url= 'https://pokemonbattle.me:9104/'

#Создание покемона
response_add_pokemon = requests.post(f'{base_url}pokemons', headers={ "trainer_token": token}, json={
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})
print(response_add_pokemon.text)

#Смена имени покемона
response_rename_pokemon = requests.put(f'{base_url}pokemons', headers={ "trainer_token": token}, json={
    "pokemon_id": "9167",
    "name": "Цветозавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})
print(response_rename_pokemon.text)


#Поймать покемона в покебол
response_add_pokeball = requests.post(f'{base_url}trainers/add_pokeball', headers={ "trainer_token": token}, json={
"pokemon_id": "9173"
})
print(response_add_pokeball.text)