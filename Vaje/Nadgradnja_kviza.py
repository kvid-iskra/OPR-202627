import requests
from deep_translator import MyMemoryTranslator
import html
import random

vpr = int(input("Koliko vprašanj želiš? "))
jezik = input("Kateri jezik vprašanj želiš vnesi sl/en: ").lower()

url = f"https://opentdb.com/api.php?amount={vpr}&type=multiple"
klic = requests.get(url).json()

translator = MyMemoryTranslator(source="english", target="slovenian")

vprasanja = klic["results"]

tocke = 0

for v in vprasanja:
    print("-" * 80)

    vprasanje = html.unescape(v["question"])

    pravilni_odgovor = html.unescape(v["correct_answer"])

    napacni_odgovori = [
        html.unescape(odgovor)
        for odgovor in v["incorrect_answers"]
    ]

    vsi_odgovori = napacni_odgovori + [pravilni_odgovor]

    if jezik == "en":

        izpis_vprasanje = vprasanje
        izpis_odgovori = vsi_odgovori
        pravilen_izpis = pravilni_odgovor

    elif jezik == "sl":

        prevodi = translator.translate_batch(
            [vprasanje] + vsi_odgovori
        )

        izpis_vprasanje = prevodi[0]

        izpis_odgovori = prevodi[1:]

        indeks_pravilnega = vsi_odgovori.index(pravilni_odgovor)
        pravilen_izpis = izpis_odgovori[indeks_pravilnega]

    else:
        print("Vnesel si neveljaven jezik!")
        break

    print(izpis_vprasanje)
    print()

    random.shuffle(izpis_odgovori)

    for i, odgovor in enumerate(izpis_odgovori):
        print(f"{i + 1} - {odgovor}")

    odgovor = int(input("Vnesi številko odgovora: "))

    if izpis_odgovori[odgovor - 1] == pravilen_izpis:
        print("Odgovor je pravilen!")
        tocke += 1
    else:
        print("Odgovor je napačen!")
        print(f"Pravilen odgovor je: {pravilen_izpis}")

print("-" * 80)
print(f"Osvojili ste {tocke} od {vpr} točk!")