# API
import requests

base_url = "https://api.chucknorris.io/jokes/random"

call = requests.get(base_url)

print(type(call.text)) #Preverimo vsebino klica

callJSON = call.json()
# print(type(callJSON))
print(callJSON["value"])