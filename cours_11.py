def write_n_numbers(filename, n):
    fichier = open(filename, "w")
    for i in range(n+1):
        fichier.write(f"{i} ")


def copy_without_space(filename1, filename2):
    file1 = open(filename1, "r")
    file2 = open(filename2, "a")
    file2.write(file1.read().replace(" ", ""))


def read_n_last_lines(filename, n):
    f = open(filename, "r")
    lst = f.readlines()
    print(lst[-n::])


read_n_last_lines("tkt", 3)
