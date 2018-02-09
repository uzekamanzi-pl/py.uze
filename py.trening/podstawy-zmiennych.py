# -*- coding: utf-8 -*-

#Podsumowanie 2 lekcji z codeacademy
import time
from datetime import datetime
now = datetime.now()
today = datetime.today()
user = input('Jak masz na imię? ')

print ('Witaj %s, jest godzina: %s:%s:%s' % (user.upper(), now.hour, now.minute, now.second))
print ('Twoje imię składa się z %s liter.' % (len(user)))

print (today)
