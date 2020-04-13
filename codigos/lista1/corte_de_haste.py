import sys

sys.setrecursionlimit(10000)

has = []
lista = []


def corte(x):
    has[0] = 0
    for y in range(1, x + 1):
        cont = -1
        for z in range(y):
            cont = max(cont, lista[z] + has[y - (z + 1)])
        has[y] = cont
    return has[x]


tam = int(input())
while tam != 0:
    lista = []
    has = [1] * (tam + 1)
    for i in range(tam):
        lista.append(int(input()))


    print(corte(tam))
    tam = int(input())