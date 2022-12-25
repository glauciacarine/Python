import requests

url = 'https://pokeapi.co/api/v2/pokemon/{}'
r = requests.get(url.format(99))
dados = r.json()
print(dados['name'])