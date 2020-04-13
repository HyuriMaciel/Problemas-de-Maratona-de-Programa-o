class Node:
    def __init__(self, org, to, time):
        self.org = org
        self.to = to
        self.time = time


def init_array(n, v=0):
    return [v for j in range(n)]


def bellman_ford(n, m, adj_list):
    dis = [0] + init_array(1999, float('inf'))

    for i in range(n):
        for j in range(m):
            if dis[adj_list[j].org] < float('inf'):
                if dis[adj_list[j].org] + adj_list[j].time < dis[adj_list[j].to]:
                    dis[adj_list[j].to] = dis[adj_list[j].org] + adj_list[j].time

    for i in range(m):
        if dis[adj_list[i].org] + adj_list[i].time < dis[adj_list[i].to]:
            return True
    return False


tests = int(input())

for i in range(tests):
    n_systems, n_hole = input().split(' ')
    n_systems, n_hole = int(n_systems), int(n_hole)

    link = []

    for j in range(n_hole):
        a, b, time = input().split(' ')
        a, b, time = int(a), int(b), int(time)

        link.append(Node(a, b, time))

    print('possible' if bellman_ford(n_systems, n_hole, link) else 'not possible')
