def licz_srednia_zarobkow(*args):
    if len(args) == 0:
        print('wpisz parametr')
        return None
    else:

    suma = 0
    for kwota in args:
        suma += kwota
    return suma / len(args)

print(licz_srednia_zarobkow(1200, 3000, 4500, 2000))
print(licz_srednia_zarobkow(7000, 6500, 5400, 10000))
print(licz_srednia_zarobkow())
