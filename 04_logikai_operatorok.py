"""
Összehasonlító operátorok
==	egyenlő
!=	nem egyenlő
<	kisebb
>	nagyobb
<=	kisebb vagy egyenlő
>=	nagyobb vagy egyenlő

Logikai operátorok
and	és
or	vagy
not	nem
"""

x = 5
y = -3

# if x < 0 and y < 0:
#     print('mindkettő negatív')

# if x < 0 or y < 0:
#     print('van köztük negatív')

# if not x <= 0:
#     print('x pozitív')

"""
1. Feladat
Készíts egy programot, amely a felhasználótól bekér egy egész számot, majd megvizsgálja, hogy a megadott szám
- pozitív páros vagy
- negatív páratlan.
Az eredményről tájékoztatja a felhasználót.
"""

# x = int(input('Adj meg egy számot! '))
#
# if x % 2 == 0 and x > 0:
#    print('Ez a szám pozitív és páros.')
# elif x % 2 != 0 and x < 0:
#    print('A szám negatív és páratlan')
# else:
#    print('Helytelen bevitel.')


"""
2. Feladat
Készíts egy programot, amely a felhasználótól két külön kérdésben megkérdezi, hogy az ikrek (Henrik és Hanna) jönnek-e ma kosrazni! 
Például így: Jön Henrik ma kosarazni? (igen/nem). A program írja ki, hogy melyik állítás igaz az alábbiak közül:
- egyikük sem jön kosarazni,
- mind a ketten jönnek kosarazni,
- csak az egyikük jön kosarazni.
"""

# hanna = input('Jön ma Hanna kosarazni? ')
# henrik = input('Jön ma Henrik kosarazni? ')

# hanna_lowercase = hanna.lower()
# henrik_lowercase = henrik.lower()

# if hanna_lowercase == 'igen' and henrik_lowercase == 'igen':
#     print('Mind a ketten jönnek kosarazni.')
# elif hanna_lowercase == 'nem' and henrik_lowercase == 'nem':
#     print('Egyikük sem jön kosarazni.')
# else:
#     print('Csak az egyikük jön kosarazni.')

"""
3. Feladat
Készíts egy programot, amely a felhasználó által megadott egész számról eldönti, hogy
- csak 3-mal osztható,
- csak 4-gyel osztható,
- 3-mal és 4-gyel is osztható,
- sem 3-mal, sem 4-gyel nem osztható!
"""

szam = int(input('Adj meg egy számot! '))

if szam % 3 == 0 and szam % 4 != 0:
    print('Ez a szám osztható 3-mal.')
if szam % 4 == 0 and szam % 3 != 0:
    print('Ez a szám osztható 4-gyel.')
if szam % 3 == 0 and szam % 4 == 0:
    print("Ez a szám osztható 3-mal és 4-gyel is.")
if szam % 3 != 0 and szam % 4 != 0:
    print('Ez a szám nem osztható sem 3-mal, sem 4-gyel.')
