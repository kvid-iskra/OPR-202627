import requests

imena = ["Vid"]

for i in imena:
    response = requests.get("https://api.agify.io", params={"name": i})
    odgovor = response.json()
    name = odgovor["name"]
    count = odgovor["count"]
    age = odgovor["age"]
    print(f"Ime: {name}, Vseh imen: {count}, Povprečna starost: {age} let")

