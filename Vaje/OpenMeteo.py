import requests

def trenutna_temp(lat, lon):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m&timezone=auto&forecast_days=1"
    call = requests.get(base_url).json()
    print(call["current"]["temperature_2m"])

def temparatura_7dni(lat, lon):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min"
    call = requests.get(base_url).json()
    print(call["daily"]["time"], call["daily"]["temperature_2m_max"])

#trenutna_temp(46.23887, 14.35561)
temparatura_7dni(46.23887, 14.35561)