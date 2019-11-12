

class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0
        self.left = None
        self.right = None


class segmentTree(object):
    def __init__(self, vector):
       # print("----",nums)

        def createTree(vector, left, rigth):
            #print(l,r)
            if left > rigth:
                return None

            if left == rigth:
                n = Node(left, rigth)
                n.sum = vector[left]
                return n

            mid = (left + rigth) // 2

            st = Node(left, rigth)
            st.left = createTree(vector, left, mid)
            st.right = createTree(vector, mid +1, rigth)

            st.sum = st.left.sum + st.right.sum

            return st

        self.st = createTree(vector, 0, len(vector) -1)

    def update(self, current, val):

        def updateVal(st, current, val):

            if st.start == st.end:
                st.sum = val
                return val
            mid = (st.start + st.end) // 2

            if current <= mid:
                updateVal(st.left,current, val)
            else:
                updateVal(st.right, current, val)
            st.sum = st.left.sum + st.right.sum
            return st.sum

        return updateVal(self.st, current, val)

    def sumRange(self, i, j):

        def rangeSum(st, i, j):

            if st.start == i and st.end == j:
                return st.sum

            mid = (st.start + st.end) // 2

            if j <= mid:
                return rangeSum(st.left, i, j)

            elif i >= mid + 1:
                return rangeSum(st.right, i, j)

            else:
                return rangeSum(st.left, i, mid) + rangeSum(st.right, mid +1, j)

        return rangeSum(self.st, i, j)


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

def mergesort(A, aux, start, end):
    if end <= start:
        return
    meio = (start+ end) // 2

    mergesort(A, aux, start, meio)

    mergesort(A, aux, meio + 1, end)

    merge(A, aux, meio, start,  end)



# n = int(input())
# A = input()
# A = A.split(' ')
#
# for i, e in enumerate(A):
#     A[i] = int(e)
# #print(A)
# q = int(input())
#
# R = []
#
# for i in range(q):
#     R.append((input()).split())
# tree = segmentTree(A)


n = 8
A = [1,5,6,7,1,2,3,4]
q = 5
R = [["Q","0","7"],["Q","0","4"],["U","1","-10"],["Q","1","2"],["Q","1","7"]]
#print(R)
#print(R[0][1])


tree = segmentTree(A)


def min_value(aux):
    aux2 = []
    for i in range(len(aux)):
        aux2.append(0)

    mergesort(aux,aux2,0,len(aux)-1)



for i in range(q):
    if(R[i][0] == "Q"):

        x= int(R[i][1])
        y = int(R[i][2]) + 1
        aux = A[x:y]
        min_value(aux)

        print(tree.sumRange(int(R[i][1]), int(R[i][2])),aux[0])

    elif(R[i][0] == "U"):

        aux = int(R[i][2])
        A[int(R[i][1])] = aux

        tree.update(int(R[i][1]), int(R[i][2]))


