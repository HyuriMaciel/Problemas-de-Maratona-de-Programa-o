








n = list(map(int, input().split()))

peso = list(map(int, input().split()))
A = []
for i in range(n[1]):
    A.append(input().split())

lista = []

for i in range(n[1]):
    d = []
    for j in range(2):
        d.append(int(A[i][j]))
    lista.append(d)

#print(n)
#print(peso)
#print(A)
#print(lista)


grafo = []

for i in range(n[1]):
    grafo.append([0]*(n[1]+1))

#print(grafo)


for i in range(n[1]):
    x = lista[i][0]
    y = lista[i][1]
    if peso[x-1] <= peso[y - 1]:
        grafo[x - 1][y - 1] = peso[x - 1]
    else:
        grafo[x - 1][y - 1] = peso[y - 1]

#print(grafo)

entidade = 0
for i in range(n[1]):
    x = lista[i][0]
    y = lista[i][1]
    entidade += grafo[x - 1][y - 1]


print(entidade)

