from random import randint


def create_matrix(r, c):
    lst = []
    for i in range(r):
        lst.append([])
        for j in range(c):
            lst[i].append(randint(0, 100))

    return lst


def get_row(m, r):
    return m[r]


def get_column(m, c):
    lst = []
    for i in m:
        lst.append(i[c])
    return lst


def print_matrix(m):
    for i in m:
        for j in range(len(i)):
            print(i[j], end=" ")
        print("")


def add_matrix(m1, m2):
    lst = []
    if (len(m1) != len(m2)) or (len(m1[0]) != len(m2[0])):
        return "c'est ciao"
    for i in range(len(m1)):
        lst.append([])
        for j in range(len(m1[i])):
            lst[i].append(m1[i][j] + m2[i][j])
    return lst


ma1 = create_matrix(3, 3)
ma2 = create_matrix(3, 3)
print_matrix(ma1)
print()
print_matrix(ma2)
print()
print_matrix(add_matrix(ma1, ma2))

