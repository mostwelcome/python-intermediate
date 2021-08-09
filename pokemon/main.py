from requests import Request
from requests import Request
import requests
while True: 
    pokemon = input('Enter pokemon name : \n')
    response = requests.get('https://pokeapi.co/api/v2/pokemon/'+pokemon.lower())
    if response.status_code ==200:
        data = response.json()
        print(type(data))
        print(data.get('name'))
    else:
        print('pokemon not found')    
