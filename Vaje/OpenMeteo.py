import requests

def trenutna_temp(lat, lon):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m&timezone=auto&forecast_days=1"
    call = requests.get(base_url).json()
    print(call["current"]["temperature_2m"])

def temparatura_7dni(lat, lon):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min"
    call = requests.get(base_url).json()
    print(call["daily"]["time"], call["daily"]["temperature_2m_max"])

def trenutna_temp2(lat, lon):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude" : lat,
              "longitude" : lon,
              "current" : "temperature_2m,rain",
              "timezone" : "auto",
              "forecast_days" : 1}
    call = requests.get(base_url, params=params)
    json = call.json()
    return json["current"]["temperature_2m"], json["current"]["rain"]
    #print(call.url)

cities = [
    ("Ljubljana", 46.0511, 14.5051),
    ("Maribor", 46.5558, 15.6459),
    ("Celje", 46.2309, 15.2604),
    ("Kranj", 46.2389, 14.3556),
]

temperatures = []

for name, lat, lon in cities[:4]:
    t = (trenutna_temp2(lat, lon))
    temperatures.append((name, t))
    print(name, t)


najvecjat = max(temperatures, key=lambda x: x[1][0])
najmanjsat = min(temperatures, key=lambda x: x[1][0])
najvecjid = max(temperatures, key=lambda x: x[1][1])
najmanjsid = min(temperatures, key=lambda x: x[1][1])
print("Najvišja temperatura je v:", najvecjat[0], "=", najvecjat[1][0], "°C")
print("Najnižja temperatura je v:", najmanjsat[0], "=", najmanjsat[1][0], "°C")
print("Najmanj dežja je v:", najmanjsid[0], "=", najmanjsid[1][1])
print("Največ dežja je v:", najvecjid[0], "=", najvecjid[1][1])

#trenutna_temp(46.23887, 14.35561)
#temparatura_7dni(46.23887, 14.35561)
#trenutna_temp2(46.23887, 14.35561)






#https://hackmd.io/@lukac/api1