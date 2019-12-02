def createTree(i, l, r,A):

    if l == r:
        tree[i] = A[l] % 2
        return
    else:
        mid = (l + r) // 2
        createTree(i*2, l, mid, A)
        createTree((i*2)+1, mid+1, r, A)
        tree[i] = comp(tree[i*2], tree[(i*2)+1])

def update(i,l,r, pos,val):

    if(l > pos or r < pos):
        return
    if l == r:
        tree[i] = val % 2
    else:
        mid = (l + r) // 2
        update(i * 2, l, mid, pos, val)
        update((i * 2) + 1, mid + 1, r, pos, val)
        tree[i] = comp(tree[i * 2], tree[(i * 2) + 1])


def sumRange(i,l,r,L,R):

    if (R < l or L > r):
        #return 1
        return 0
    elif (l >= L and r <= R):
        return tree[i]
    mid = (l+r) // 2
    return comp(sumRange((i*2),l,mid,L,R) , sumRange((i*2)+1,mid+1,r,L,R))


def comp(a,b):
    return a + b

def queryOder(l,r):
    return sumRange(1,0,len(A)-1,l,r)

def queryP(l,r):
    return(r - l + 1) - queryOder(l,r)


#
# createTree(1,0,len(A)-1, A)
# print(tree)
#
# # update(1,0,len(A)-1,1,4)
# # print(tree)
# #print(sumRange(1,0,len(A)-1,1,2))
#
#
#
# print(queryP(1,3))
#
# print(queryOder(1,3))



n = int(input())

A = list(map(int, input().split()))

n = len(A)
tree =[0 for i in range(4*n)]

createTree(1,0,len(A)-1, A)

q = int(input())

R = []

for i in range(q):
   R.append((input()).split())

i = 1
for i in range(q):
    if(int(R[i][0]) == 1):
        l = int(R[i][1]) - 1
        r = int(R[i][2]) - 1
        print(queryP(l,r))

    elif(int(R[i][0]) == 2):
        l = int(R[i][1]) - 1
        r = int(R[i][2]) - 1
        print(queryOder(l,r))

    elif(int(R[i][0]) == 0):
        l = int(R[i][1])-1
        r = int(R[i][2])
        update(1,0,len(A)-1,l,r)
