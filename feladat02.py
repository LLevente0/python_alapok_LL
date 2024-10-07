"""1. Feladat
Python fejlesztői környezetben készíts egy rövid programot,
amely a felhasználótól bekéri a kör sugarát, és ennek alapján kiszámolja a kör kerületét és területét!"""

r = input('Add meg a kör sugarát: ')

# Kör kerülete
print('Kör kerülete:')
print(2 * int(r) * 3.14)

# Kör területe
print('Kör területe:')
print(int(r) * int(r) * 3.14)


"""2. Feladat
Írj egy programot, ami a felhasználótól bekéri először a keresztnevét, 
majd a vezetéknevét. A program ezután összefűzi ezeket egy teljes_nev nevű változóba. 
Végül a program a teljes nevén üdvözli a felhasználót!"""


vezeteknev = input('Add meg a vezetékneved: ')
keresztnev = input('Add meg a keresztneved: ')

teljes_nev = vezeteknev + ' ' + keresztnev
print('Üdvözöllek' , teljes_nev + '!')


"""3. Feladat
Írj egy programot, ami bekér egy számot a felhasználótól, 
és valamilyen matemataikai műveletek sorozataként generál és kiír a felhasználónak egy szerencseszámot!"""

szerencseszam = input('Adj meg egy számot: ')
print(int(szerencseszam) * 2 * 4 / 3)
