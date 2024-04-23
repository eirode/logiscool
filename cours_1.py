"""def pair_impair(nbr):
    if nbr % 2 == 0:
        return 'Pair'
    else:
        return 'Impair'


print(pair_impair(3))"""


"""def triangle_rectangle(a, b, c):
    if a ** 2 == b ** 2 + c ** 2:
        return "oui hyp = a"
    elif b ** 2 == a ** 2 + c ** 2:
        return "oui hyp = b"
    elif c ** 2 == a ** 2 + b ** 2:
        return "oui hyp = c"
    else:
        return "non"


print(triangle_rectangle(5, 4, 3))"""


"""def convert(miles):
    km = miles * 1.609344
    return km


mls = int(input("entrez le nombres de miles à convertir\n"))
print(convert(mls))"""


"""def maj_min(phrase):
    low = 0
    up = 0
    for i in phrase:
        if i.islower():
            low += 1
        elif i.isupper():
            up += 1
    return low, up


low, up = maj_min("Bonjour MosieURS")
print(f"il y a {up} majuscules et {low} minuscules")"""


"""def invert_string(phrase):
    inverse = ""
    for i in phrase:
        inverse = i + inverse

    return inverse


print(invert_string("python"))"""


def plus_grand(a, b, c):
    lst = [a, b, c]
    maxi = 0
    for i in range(len(lst)):
        if lst[i] > maxi:
            maxi = lst[i]


    return maxi, lst
