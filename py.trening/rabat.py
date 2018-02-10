brutto = input('podaj kwote brutto ')
rabat = input ('podaj rabat w % ')

netto = int(brutto) / 1.23

print ('kwota netto przed rabatem: %s' % (netto))

vat = int(brutto) - int(netto)

print ('kwota VAT przed rabatem wynosi: %s' % (vat))

brutto = int(brutto) - int(brutto) * int(rabat) /100

print ('kwota brutto po rabacie: %s' % (brutto))

netto = int(brutto) / 1.23

print ('kwota netto po rabacie: %s' % (netto))

vat = int(brutto) - int(netto)

print ('kwota VAT po rabacie wynosi: %s' % (vat))