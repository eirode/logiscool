from random import randint

incomes = [
    [10000, 10000, 65489, 223344, 987654],
    [84536, 987631, 758569, 98536, 436656],
    [64538, 525329, 966494, 421412, 98655],
    [865947, 924456, 214532, 126975, 5456]
]

lst = []

def taxes(nbr):
    if nbr <= 85430:
        tax = nbr / 100
        tax = tax * 18
        tax -= 560

    else:
        surp = ((nbr - 85430) / 100) * 27
        tax = 14900 + surp

    if tax <= 0:
        tax = 0

    return tax


def moyenne(temper):
    lst = []
    tot = 0
    moye = 0
    for i in temper:
        for j in i:
            tot += j

        moye = tot/24
        lst.append(moye)

    return lst


for i in range(101):
    if i % 2 == 0:
        lst.append(i)

lst_comp = [[i for i in range(j*3, (j*3)+3)] for j in range(3)]

temp = [[randint(-5, 32) for i in range(24)] for j in range(30)]
for i in temp:
    print(i)

print(moyenne(temp))