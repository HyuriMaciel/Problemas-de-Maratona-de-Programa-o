sys.setrecursionlimit(15000)
p = 0
f = 0
e = 0
a = 0
trade = 0
pd = [[int(0) for i in range(21)] for j in range(5001)]
vec = [[] for i in range(5001)]


def knap(pp, ff):
    if pp == p + 1:
        pd[pp][ff] = 0
        return pd[pp][ff]

    if pp == p:
        aa = float('inf')
        for i in range(f):
            aaa = vec[pp][i]
            if i != ff:
                aaa += trade
            aa = min(aaa, aa)
        pd[pp][ff] = aa

    if pd[pp][ff] != -1:
        return pd[pp][ff]

    aa = float('inf')

    for i in range(f):
        aaa = knap(pp + 1, i) + vec[pp][i]
        if i != ff:
            aaa += trade
        aa = min(aa, aaa)

    pd[pp][ff] = aa

    return pd[pp][ff]


while True:
    read = [int(i) for i in input().split(' ')]
    f, p, e, a = read

    if a + p + f + e == 0:
        break

    trade = e * a

    for i in range(p):
        for j in range(f):
            pd[i][j] = -1
    for i in range(1, p + 1):
        for j in range(f):
            zz = [int(i) for i in input().split(' ')]
            aa, bb = zz
            vec[i].append(aa * bb)

    knap(1, 0)

    aa = float('inf')
    for i in range(f):
        if pd[1][i] == -1:
            continue
        aa = min(aa, pd[1][i])

    print(aa)

    pd = [[int(0) for i in range(21)] for j in range(5001)]
    vec = [[] for i in range(5001)]