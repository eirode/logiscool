import math
import random as rnd
import matplotlib.pyplot as plt
lst = []

def aire(r):
    return r ** 2 * math.pi


def perimetre(r):
    return 2 * math.pi * r


def fill_list():
    for i in range(100):
        lst.append(rnd.randrange(0, 10, 2))


explosion = (0, 0.3, 0.1)
rate = [15, 35, 50]
label = ["le premier", "le deuxième", "le troisième"]
diagram = plt.pie(rate, labels=label, autopct='%0.f%%',
                  colors=["red", "pink", "yellow"])
plt.show()
