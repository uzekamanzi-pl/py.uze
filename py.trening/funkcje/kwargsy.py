studenci = {
    'Alicja': {'wiek': 21, 'kierunek': 'informatyka', 'ocena': 4},
    'Kasia': {'wiek': 23, 'kierunek': 'ekonomia', 'ocena': 4},
    'Zygfryd': {'wiek': 99, 'kierunek': 'archeologia', 'ocena': 3},
    'Tomek': {'wiek': 25, 'ocena': 2}
}

def pokaz_wszystkie(studenci):
    for klucz, wartosc in studenci.items():
        print(klucz, wartosc)

pokaz_wszystkie(studenci)


##for klucz in studenci.keys():


print(studenci.items())

print(studenci.values())

print(len(studenci.items()))