# -*- coding: utf-8 -*-

woda = input('Czy jest woda w czajniku? ')

if woda == "tak" or woda == "Tak":
    print ('Świetnie')
elif woda == "nie" or woda =="Nie":
    print ('Nalej wody')

gaz = input('Czy gaz jest włączony? ')

if gaz == "tak" or gaz == "Tak":
    print ('Wspaniale, gaz włączony')
elif gaz == "nie" or gaz =="Nie":
    print ('Włącz gaz')

czajnik = input('Czy czajnik stoi na gazie? ')

if czajnik == "tak" or czajnik == "Tak":
    gwizdek = input('Czy czajnik gwiżdże? ')
    if gwizdek == "tak" or gwizdek == "Tak":
        print('Wspaniale, wyłącz gaz')
    elif gwizdek == "nie" or gwizdek == "Nie":
        print('Czekaj z uśmiechem')

elif gaz == "nie" or gaz =="Nie":
    print ('Włącz gaz')
