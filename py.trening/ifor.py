number = input('podaj liczbe')

if int(number) > 0:
    print('liczba jest wieksza od zera')

elif int(number) == 0:
    print('podana liczba to zero')

elif int(number) < 0:
    print('podana liczba jest mniejsza od zera')

else:
    print('nie wprowadziłeś liczby')

