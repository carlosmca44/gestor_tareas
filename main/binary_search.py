import math


def binary_seacrh(list, x):
    izq = 0
    der = len(list)-1

    if len(list) == 1 and list[0] == x:
        return 0

    while izq < der:
        medio = (izq+der)/2
        medio = math.ceil(medio)

        if list[izq] == x:
            return izq

        if list[der] == x:
            return der

        if list[medio] == x:
            return medio
        elif list[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1

    return -1
