import requests
from pprint import pprint
import html
import random
 
vpr = int(input("Koliko vprašanj želiš? "))
url = f"https://opentdb.com/api.php?amount={vpr}&type=multiple"
klic = requests.get(url).json()
 
vprasanja = klic["results"]

tocke = 0
 
for v in vprasanja:
    print("-"*80)
    #pprint(v)
    #print("-"*80)
 
    print(html.unescape(v["question"]))  #odstrani HTML znake
    pravilni_odgovor = v["correct_answer"]
    napacni_odgovori = v["incorrect_answers"]
    pravilen_odgovor_seznam = [pravilni_odgovor]
    vsi_odogovori = napacni_odgovori + pravilen_odgovor_seznam
    random.shuffle(vsi_odogovori)
 
    prav = pravilni_odgovor
    odgovori = [vsi_odogovori[0], vsi_odogovori[1], vsi_odogovori[2], vsi_odogovori[3]]
    for i, o in enumerate(odgovori):
        print(f"{i+1} - {o}")
    odgovor = int(input("Odgovor: "))
    if prav == odgovori[odgovor-1]:
        print("Odogovor je pravilen!")
        tocke += 1
    else:
        print("Odgovor je napačen!")

print(f"Osvojili ste {tocke} točk")