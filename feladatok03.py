"""1.1 Feladat
Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e!
A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép!"""

"""1.2 Feladat
Fejleszd tovább az első feladat programját úgy, hogy amennyiben a felhasználó 
nem a két lehetséges válasz (igen/nem) 
közül ad meg egyet, a gép kiírja: "Sajnos nem értem a válaszodat!"""


nap = input('Jó napod van? ')
nap_lowercase = nap.lower()
if nap_lowercase == 'nem':
    print('Gatyaa')
if nap_lowercase == 'igen':
    print('Király')
else:
    print('Sajnos nem értem a válaszodat')


"""2. Feladat
Készíts egy programot, ami bekér egy számot a felhasználótól, majd kiírja, 
hogy a megadott szám páros-e vagy páratlan!"""


szam = int(input('Adj meg egy számot! '))
if szam % 2 == 0:
    print('Ez a szám páros')
else:
    print('Ez a szám páratlan')
