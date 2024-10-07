"""1. Feladat
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot,
majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal!
Az összehasonlítás eredményéről tájékoztassa a felhasználót!"""

import random

szam = int(input("Adj meg egy számot: "))

random_szam = random.randint(1, 3)
print(random_szam)

if szam == random_szam:
    print("A két szám megegyezik.")
if szam != random_szam:
    print('A két szám nem egyezik meg.')



"""2. Feladat
A program a pénzfeldobást modellezi. 
Kérdezze meg a felhasználótól a választását (fej vagy írás),
 majd adjon tájékoztatást, hogy eltalálta-e!"""

fej_vagy_iras = input("Fej vagy írás? ")

import random

random_dobas = random.randint(1, 2)

if random_dobas == 1:
    print('fej')
if random_dobas == 2:
    print('írás')
if random_dobas == fej_vagy_iras:
    print("Eltaláltad!")
else:
    print('Nem találtad el!')

