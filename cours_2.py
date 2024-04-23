def boucle(n):
    print(n)
    if n > 0:
        boucle(n - 1)


def facto(n):
    if n == 1:
        return 1
    else:
        return n * facto(n - 1)


def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


def somme_inverse(n):
    if n == 1:
        return 1
    else:
        return 1 / n + somme_inverse(n - 1)
