
MAX = 10**5 + 1
dl = [0 for i in range(MAX)]

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




def deletevictory(a ,b):
    #print(b)
    if a != 0 and b != 0:
        l = input()
        B = [int(i) for i in l]
        lista = B[:]
        aux = []
        aux = [0 for i in range(a)]
        mergesort(B, aux, 0, len(B) - 1)
        #print(lista)
        #print(B)
        for i in range(b):
            a = B[i]
            #print(a)
            lista.remove(a)

        for j in range(len(lista)):
            print(lista[j], end="")
        print()

        A = list(map(int, input().split()))
        deletevictory(A[0], A[1])
    else:
        return



A = list(map(int, input().split()))

deletevictory(A[0],A[1])