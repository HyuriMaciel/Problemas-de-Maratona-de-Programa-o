def search_binary_higth(A, left, higth, value):

    if higth < left:
        #print(left, higth)
        return higth
    mid = round((left + higth) / 2)
    if A[mid] == value:
        if mid <= len(A)-1:
           return search_binary_higth(A, mid + 1, higth, value)

    elif A[mid] > value:
        return search_binary_higth(A, left, mid - 1, value)
    else:
        return search_binary_higth(A, mid + 1, higth, value)



def search_binary_left(A, left, higth, value):

    if higth < left:
        #print(left, higth)
        return left
    mid = (left + higth) // 2
    #mid = round((left + higth) / 2)
    if A[mid] == value:

        if mid >= 0:
            return search_binary_left(A, 0, mid - 1, w)

    elif A[mid] > value:
        return search_binary_left(A, left, mid - 1, value)
    else:
        return search_binary_left(A, mid + 1, higth, value)

#A = [ 1,1,1,2,5,6,6,7]
#w = 3
I = []

size = int(input())

A = input()

A = A.split(' ')

for i, e in enumerate(A):
    A[i] = int(e)

quant = int(input())

for i in range(quant):
    I.append(int(input()))

for i in range(quant):
    w = I[i]

    hi = search_binary_higth(A, 0 , len(A)-1, w)
    lo = search_binary_left(A, 0 , len(A)-1, w)


    print(lo,hi)
