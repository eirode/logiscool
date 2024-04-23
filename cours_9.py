def mult(tupl, nbr):
    lst = list(tupl)
    lst_result = []
    for i in lst:
        lst_result.append(i * nbr)

    return tuple(lst_result)


# print(mult((4, 2, 3), 8))

def concat_square(tupl):
    tupl2 = []
    for i in tupl:
        tupl2.append(i ** 2)
    return tupl + tuple(tupl2)


print(concat_square((1, 2, 3)))

def make2d(tupl, nbr):
    lst = []
    for i in range(nbr):
        lst.append([])
        for j in tupl:
            lst[i].append(j*(i+1))
        lst[i] = tuple(lst[i])

    return tuple(lst)


print(make2d((1, 2, 3), 3))
