entrada = list(map(int, input().split()))
n = entrada[0]
m = entrada[1]

queue = []
grafo = []
for i in range(n):
        grafo.append([])

indegree = [0] * n
visited = [0] * n

for i in range(m):
    linha = list(map(int, input().split()))
    v = linha[0]-1
    u = linha[1]-1
    grafo[u].append([v])
    indegree[v] += 1

for i in range(n):
    if indegree[i] == 0:
        queue.append(i+1)


top_order = []
while queue:
    u = queue.pop(queue.index(min(queue)))

    top_order.append(u)
    visited[u-1] = 1
    for i in grafo[u-1]:
        if visited[i[0]] == 0:
            indegree[i[0]] -= 1
            if indegree[i[0]] == 0:
                queue.append(i[0]+1)

if len(top_order) == n:
    print(' '.join([str(elem) for elem in top_order]))
else:
    print("Impossible")

