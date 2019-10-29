def search_binary(A, left, higth, value):

    # item não está presente.
    if higth < left:
        print(higth, left)
        return -1
    mid = (left + higth) // 2
    # o elemento está no meio do arranjo.
    if A[mid] == value:
        return mid
    elif A[mid] > value:
        return search_binary(A, left, mid - 1, value)
    else: # A[meio] < item
        return search_binary(A, mid + 1, higth, value)


A = []
I = []

tam = int(input("quantidade do dinheiro"))

#A = [int(i) for i in input().split()]

for i in range(tam):
    A.append(int(input()))

quant = int(input("quantidade de indesição"))

for i in range(quant):
    I.append(int(input()))

for i in range(len(I)):
    w = I[i]
    x = search_binary(A, 0, len(A) - 1, w)
    y = x
    z = int(len(A))

    lo = x
    hi = x

    if (x != -1):
        while x >= 0:
            if (A[x] == w):
                lo = x
            x = x - 1

        while y < z:
            if (A[y] == w):
                hi = y
            y = y + 1

        print(lo, hi)
        i = i + 1













