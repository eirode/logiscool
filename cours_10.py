def prendre_note(nbr):
    lst = []
    for i in range(nbr):
        note = int(input(f"donnez la {i+1} er/ème note sur 100\n"))
        lst.append(((i+1), note))
    return lst


def note_to_mention(lst, eleve):
    note = lst[eleve-1][1]
    if note > 90:
        return f"la note de l'élève {eleve} est A+"
    elif note > 70:
        return f"la note de l'élève {eleve} est A"
    elif note > 60:
        return f"la note de l'élève {eleve} est B+"
    elif note > 50:
        return f"la note de l'élève {eleve} est B"
    elif note > 30:
        return f"la note de l'élève {eleve} est F+"
    else:
        return f"la note de l'élève {eleve} est F"


def note_to_mention_v2(lst, eleve):
    note = lst[eleve-1][1]
    if note > 90:
        return "A+"
    elif note > 70:
        return "A"
    elif note > 60:
        return "B+"
    elif note > 50:
        return "B"
    elif note > 30:
        return "F+"
    else:
        return "F"


def plus_elevee(lst):
    plus_grand = -10
    for i in lst:
        if i < plus_grand:
            plus_grand = i


def plus_basse(lst):
    plus_bas = -10
    for i in lst:
        if i < plus_bas:
            plus_bas = i


def moyenne(lst):
    tot = 0
    for i in range(len(lst)):
        tot += lst[i][1]

    print(len(lst))
    return tot / len(lst)


def same(t1, t2):
    if len(t1) != len(t2):
        return False
    for i in t1:
        if i not in t2:
            return False
    return True


tuple_binaire = (0, 1, 0, 1, 1)

