import random

"""def carre(n):
    for i in range(n):
        yield i**2


for i in carre(100000):
    print(i)"""

"""def pairs(n):
    for i in n:
        if i % 2 == 0:
            yield i


lst = [1, 7, 5, 8, 0, 4, 7, 4, 165, 154, 965, 768, 652, 9198687548]

for i in pairs(lst):
    print(i)"""

lst_art = ["beurre", "lait", "trésor", "eau", "haribo", "pain"]
lst_prix = [5, 6, 10, 3, 6, 3]

def jsp():
    nbr = int(input("combien d'article voulez vous acheter? "))
    lst_art_ach = []
    lst_nbr_ach = []
    tot_art = 0
    prix = 0
    while tot_art < nbr:
        # lst_art_ach.append(n[random.randint(0, 5)])
        while True:
            j = random.randint(0, 5)
            jl = lst_art[j]
            if jl not in lst_art_ach:
                lst_art_ach.append(jl)
                break
        alea = random.randint(1, nbr - tot_art)
        lst_nbr_ach.append(alea)
        tot_art += alea
        prix += lst_prix[j] * alea

    print(lst_art_ach)
    print(lst_nbr_ach)
    print(prix)

import matplotlib


def maximum(liste):
    maxi = liste[0]
    for i in liste[1:]:
        if i > maxi:
            maxi = i
    return maxi


jsp()
