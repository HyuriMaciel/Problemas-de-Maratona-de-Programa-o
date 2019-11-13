def createTree(i, l, r,A):

    if l == r:
        tree[i] = A[l]
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
        tree[i] = val
    else:
        mid = (l + r) // 2

        update((i * 2), l, mid, pos, val)
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





def createTree2(i, l, r,A):

    if l == r:
        tree2[i] = A[l]
        return
    else:
        mid = (l + r) // 2
        createTree2(i*2, l, mid, A)
        createTree2((i*2)+1, mid+1, r, A)
        tree2[i] = min(tree2[i*2], tree2[(i*2)+1])

def update2(i,l,r, pos,val):

    if(l > pos or r < pos):
        return
    if l == r:
        tree2[i] = val
    else:
        mid = (l + r) // 2
        update2(i * 2, l, mid, pos, val)
        update2((i * 2) + 1, mid + 1, r, pos, val)
        tree2[i] = min(tree2[i * 2], tree2[(i * 2) + 1])


def sumRange2(i,l,r,L,R):

    if (R < l or L > r):
        #return 1
        return 0
    elif (l >= L and r <= R):
       # print(tree[i])
        return tree2[i]
    mid = (l+r) // 2
    return min(sumRange2((i*2),l,mid,L,R) , sumRange2((i*2)+1,mid+1,r,L,R))


def queryMin(a,b):
    return sumRange2(1,0,len(A)-1,a,b)

def sm(a,b):
    return sumRange(1, 0, len(A) - 1, a, b)

def comp(a,b):
   return a + b

n = 8

A = [1, 5, 6, 7, 1, 2, 3, 4]

n = len(A)
tree =[0 for i in range(4*n)]
tree2 =[0 for i in range(4*n)]

createTree(1, 0,len(A)-1, A)
createTree2(1,0,len(A)-1, A)
print(tree)
print(tree2)

q = 5
R = [["Q", "0", "7"],["Q", "0", "4"],["U","1", "-10"],["Q", "1", "2",],["Q", "1", "7"]]
#print(sumRange(1,0,len(A)-1,1-1,3))
#update(0,0,len(A)-1,1,3)
#print(sumRange(1,0,len(A)-1,1-1,3))




for i in range(q):
    if(R[i][0] == "Q"):
        l = int(R[i][1])-1
        r = int(R[i][2])-1
        print(sm(int(R[i][1]),int(R[i][2])), queryMin(int(R[i][1]),int(R[i][2])))

    elif(R[i][0] == "U"):
        l = int(R[i][1]) - 1
        r = int(R[i][2])
        update(1, 0, len(A) - 1, int(R[i][1]), r)
        update2(1, 0, len(A) - 1, int(R[i][1]), r)