

class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0
        self.par = 0
        self.impar = 0
        self.left = None
        self.right = None


class segmentTree(object):
    def __init__(self, vector):

        def createTree(vector, left, rigth):
            #print(l,r)
            if left > rigth:
                return None

            if left == rigth:
                n = Node(left, rigth)
                if vector[left] % 2 == 0:

                    n.par = 1
                else:

                    n.impar = 1
                return n

            mid = (left + rigth) // 2

            st = Node(left, rigth)
            st.left = createTree(vector, left, mid)
            st.right = createTree(vector, mid +1, rigth)

            st.par = st.left.par + st.right.par
            st.impar = st.left.impar + st.right.impar

            return st

        self.st = createTree(vector, 0, len(vector)-1)

    def update(self, current, val):

        def updateVal(st, current, val):

            if st.start == st.end:
                if val % 2 == 0:
                    st.par = 1
                else:
                    st.impar = 0

                return val
            mid = (st.start + st.end) // 2

            if current <= mid:
                updateVal(st.left,current, val)
            else:
                updateVal(st.right, current, val)
            st.par = st.left.par + st.right.par
            st.impar = st.left.impar + st.right.impar
            return st.par, st.impar

        return updateVal(self.st, current, val)

    def sumRange(self, i, j,pi):

        def rangeSum(st, i, j,pi):

            if st.start == i and st.end == j:
                if pi == 1 :
                    return st.par
                elif pi == 2:
                    return st.impar

            mid = (st.start + st.end) // 2

            if j <= mid:
                return rangeSum(st.left, i, j)

            elif i >= mid + 1:
                return rangeSum(st.right, i, j,pi)

            else:
                return rangeSum(st.left, i, mid,pi) + rangeSum(st.right, mid +1, j,pi)

        return rangeSum(self.st, i, j,pi)




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


n = 6
A = [1,2,3,4,5,6]
q = 4
R = [[1,2,5],[2,1,4],[0,5,4],[1,1,6]]



tree = segmentTree(A)


#print(tree.sumRange(int(R[0][1]),int(R[0][2]),2))
# print(tree2.sumRange2(int(R[0][1]),int(R[0][2])))

for i in range(q):
    if(R[i][0] == 1):
        if R[i][2] == A[len(A)-1]:
            print(tree.sumRange(R[i][1],R[i][2]-1,1))
        else:
            print(tree.sumRange(R[i][1], R[i][2],1))
    elif(R[i][0] == 2):
         print("impa")
        # if R[i][2] == A[len(A) - 1]:
        #      print(tree.sumRange(R[i][1], R[i][2] - 1,2))
        # else:
        #     print(tree.sumRange(R[i][1], R[i][2], 2))

    elif(R[i][0] == 0):
        tree.update(R[i][1], R[i][2])



