def combustivel(test):

    gasto = (m + test) / d[0]
    test -= gasto
    for i in range(1, len(d)):
        gasto = (m + test) / p[i]
        test -= gasto
        gasto = (m + test) / d[i]
        test -= gasto

    gasto = (m + test) / p[0]
    test -= gasto

    return test

def search_binary(l, size):
    r = combustivel(size)
    if r < 0:
        print(-1)
        exit()
        #return 0

    while (size - l) > 0.00001:

        r = (l + size) / 2

        c = combustivel(r)

        if c == 0:
            return r

        elif c > 0:
            size = r
        else:
            l = r
    return r


chute = 1000000000

n = int(input())

m = int(input())

d = list(map(int, input().split()))

p = list(map(int, input().split()))

r = search_binary(0, chute)

print('{:.2f}'.format(r))
