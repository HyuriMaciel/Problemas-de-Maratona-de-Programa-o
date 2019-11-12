def chuva_min_max(hi):
    min = [0 for i in range(len(hi) + 1)]
    min[0] = hi[0]
    aux = min[0]


    for i in range(len(hi)):
        if min[i] >= hi[i]:
            min[i + 1] = aux

        else:

            aux = hi[i]
            min[i + 1] = aux

    max = [0 for i in range(len(hi)+1)]

    max[n - 1] = hi[n - 1]

    aux2 = max[n-1]

    for i in range(len(hi) - 1, -1, -1):
        if max[i] >= hi[i]:
            max[i - 1] = aux2
        else:
            aux2 = hi[i]
            max[i-1] = hi[i]

    return min, max

def chuva(min, max,hi):
    aux = 0
    for i in range(len(hi) - 1):
        if hi[i] < min[i] and hi[i] < max[i]:
            aux = aux + 1
    print (aux)



#hi = [4,3,2,1,1,1,1,1,2,3,5,5,3,3,2,4,4]
n = int(input())
hi = []
min = [n]
max = [n]

for i in range(n):
    hi.append(int(input()))

min,max = chuva_min_max(hi)

#print (min)
#print (max)

chuva(min,max,hi)