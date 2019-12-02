def merge(l, r,sizel,sizer,size):
    global count
    a = []

    #tam = sizel + sizer
    aux1 = 0
    aux2 = 0

    for i in range(size):
        if (aux1 < sizel and aux2 < sizer):
            if (l[aux1] <= r[aux2]):
                a.append(l[aux1])
                aux1 += 1
            elif(l[aux1] > r[aux2]):
                a.append(r[aux2])
                aux2 += 1
                count += sizel - aux1
        elif (aux1 == sizel):
            while (aux2 < sizer):
                a.append(r[aux2])
                aux2+= 1
        elif (aux2 == sizer):
            while (aux1 < sizel):
                a.append(l[aux1])
                aux1 += 1
    return a

def merge_sort(A,size):
    if size == 1:
        return A
    else:
        mid = size//2
        l = A[0:mid]
        r = A[mid:size]

        L = merge_sort(l,len(l))
        R = merge_sort(r,len(r))
        return merge(L, R,len(L),len(R),len(L)+len(R))


count = 0
t = int(input())

for i in range(t):
    aleatorio = input()
    n = int(input())
    A = []
    for i in range(n):
        A.append(int(input()))

    merge_sort(A,len(A))
    print(count)
    count = 0