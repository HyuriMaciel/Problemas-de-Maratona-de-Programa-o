
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.par =0
        self.imp =0
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
                if vector[left]% 2 == 0:
                    n.par = 1
                else:
                    n.imp = 1
                n.sum = vector[left]
                return n

            mid = (left + rigth) // 2

            st = Node(left, rigth)
            st.left = createTree(vector, left, mid)
            st.right = createTree(vector, mid +1, rigth)

            st.sum = st.left.sum + st.right.sum
            st.par = st.left.par + st.right.par
            st.imp = st.left.imp + st.right.imp
            return st

        self.st = createTree(vector, 0, len(vector) -1)

    def update(self, current, val):

        def updateVal(st, current, val):
            p = 1
            i = 1
            if st.start == st.end:
                #print(st.start,st.end)
                if val % 2 == 0:
                    print(val)
                    st.par += p
                    st.sum = val
                else:
                    st.imp += i
                    st.sum = val

                return st.par,st.imp,st.sum
            mid = (st.start + st.end) // 2

            if current <= mid:
                updateVal(st.left,current, val)
            else:
                updateVal(st.right, current, val)
            st.sum = st.left.sum + st.right.sum
            st.par = st.left.par + st.right.par
            st.imp = st.left.imp + st.right.imp
            return st.par

        return updateVal(self.st, current, val)

    def sumRangep(self, i, j):

        def rangeSump(st, i, j):

            if st.start == i and st.end == j:
                #print(st.par,st.imp)
                return st.par

            mid = (st.start + st.end) // 2

            if j <= mid:
                return rangeSump(st.left, i, j)

            elif i >= mid + 1:
                return rangeSump(st.right, i, j)

            else:
                return rangeSump(st.left, i, mid) + rangeSump(st.right, mid +1, j)

        return rangeSump(self.st, i, j)

    def sumRangei(self, i, j):

        def rangeSumi(st, i, j):

            if st.start == i and st.end == j:
                #print(st.par,st.imp)
                return st.imp

            mid = (st.start + st.end) // 2

            if j <= mid:
                return rangeSumi(st.left, i, j)

            elif i >= mid + 1:
                return rangeSumi(st.right, i, j)

            else:
                return rangeSumi(st.left, i, mid) + rangeSumi(st.right, mid +1, j)

        return rangeSumi(self.st, i, j)




#n = int(input())
#A = input()
#A = A.split(' ')

#for i, e in enumerate(A):
#    A[i] = int(e)
#print(A)
#q = int(input())

#R = []

#for i in range(q):
#    R.append((input()).split())
#print(R)


n = 6
A = [1,2,3,4,5,6]
q = 4
R = [[1,2,5],[2,1,4],[0,5,4],[1,1,6]]

tree = segmentTree(A)


for i in range(q):
    if(int(R[i][0]) == 1):
        if int(R[i][2]) == A[len(A)-1]:

            print(tree.sumRangep(int(R[i][1]),int(R[i][2])-1))
        #print(tree.st.par)
        else:
            print(tree.sumRangep(int(R[i][1]), int(R[i][2])))
    elif(int(R[i][0]) == 2):
        if int(R[i][2]) == A[len(A) - 1]:
            print(tree.sumRangei(int(R[i][1]), int(R[i][2]) - 1))
        else:
            print(tree.sumRangei(int(R[i][1]), int(R[i][2])))

    elif(int(R[i][0]) == 0):
       # print(R[i][1],A[(R[i][2])])
        tree.update(int(R[i][1]), int(R[i][2]))
        #print(A)
