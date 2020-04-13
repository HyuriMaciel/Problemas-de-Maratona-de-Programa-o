entrada = list(map(int, input().split()))
n = entrada[0]
m = entrada[1]

inf = 99999

A = []

for i in range(n):
    d = []
    for j in range(n):
        d.append(inf)
    A.append(d)

for i in range(m):
    linha = list(map(int, input().split()))
    A[linha[0]][linha[1]] = linha[2]
    A[linha[1]][linha[0]] = linha[2]

for i in range(n):
    A[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            A[i][j] = min(A[i][j], A[i][k]+A[k][j])

#print(A)

l = [0 for i in range(n)]


for i in range(n):
    for j in range(n):
        if A[i][j] > l[i]:
            l[i] = A[i][j]


#print(l)
x = min(l)
print(x)