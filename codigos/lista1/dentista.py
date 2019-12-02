
def merge(A,aux,mid, start, end):
    left = start
    left_end = mid
    rigth = left_end + 1
    rigth_end = end

    possicao = start

    while left <= left_end or rigth <= rigth_end:
        if left > left_end:
            aux[possicao]=A[rigth]
            rigth += 1
            possicao += 1

        elif rigth > rigth_end:
            aux[possicao]=A[left]
            left += 1
            possicao += 1

        elif A[left] < A[rigth]:
            aux[possicao] = A[left]
            left += 1
            possicao += 1

        else:
            aux[possicao] = A[rigth]
            rigth += 1
            possicao += 1

    for j in range(start, end +1):
        A[j]= aux[j]

def mergesort(A, aux, esquerda, direita):
    if direita <= esquerda:
        return
    meio = (esquerda + direita) // 2

    mergesort(A, aux, esquerda, meio)

    mergesort(A, aux, meio + 1, direita)

    merge(A, aux, meio, esquerda,  direita)



A = []

n = int(input())

for i in range(n):
    A.append((input()).split())

#A=[[10,300],[10,100],[40,130],[120,200],[200,400],[200,300],[300,400],[400,450],[450,100]]
lista = []

for i in range(n):
    d = []
    for j in range(2):
        d.append(int(A[i][j]))
    lista.append(d)
#print(lista)
aux = []

for i in range(n):
    aux.append([0]*2)

B =[]
for i in range(n):
    a = 0
    b = []
    for j in range(1,-1,-1):
        b.append(lista[i][j])
    B.append(b)

#print(B)

mergesort(B, aux, 0, len(lista) - 1)

#print(B)

#C=[]
# matriz ao contraio
#for i in range(n-1,-1,-1):
#    add =[]
#   for j in range(2):
#        add.append(B[i][j])
#    C.append(add)


count = 0
aux = 0
for i in range(n - 1):
    #print(aux,count)
    #print(B[aux][0],B[i+1][1])
    if B[i+1][1] >= B[aux][0]:
        count += 1
        aux = i + 1
print(count + 1)