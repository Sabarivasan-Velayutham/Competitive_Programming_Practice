

from regex import P


inf = 999
n = 6
g = [[0 for i in range(n)] for j in range(n)]
g = [[0, 16, 13, 0, 0, 0], 
     [0, 0, 10, 12, 0, 0], 
    [0, 4, 0, 0, 14, 0],
     [0, 0, 9, 0, 0, 20], 
     [0, 0, 0, 7, 0, 4], 
     [0, 0, 0, 0, 0, 0]]


def fordful(g, s, d):
    v1 = 0
    v2 = 0
    parent = [0]*(len(g))
    maxflow = 0
    rg = g
    while(bfs(g, s, d, parent)):
        pathflow = inf
        v1 = d
        while (not v1 == s):
            v2 = parent[v1]

            pathflow = min(pathflow, rg[v2][v1])
            v1 = parent[v1]
        maxflow += pathflow
        v2 = d
        while v2 != s:
            u = parent[v2]
            rg[u][v2] -= pathflow
            # rg[v2][u] += pathflow
            rg[v2][v2] += pathflow
            v2 = parent[v2]
    return maxflow


def bfs(g, s, d, parent):
    visit = [0 for i in range(n)]
    queue = []
    queue.append(s)
    visit[s] = True
    parent[s] = -1
    while queue:
        u = queue.pop(0)
        for v in range(n):
            if (not visit[v] and g[u][v] > 0):
                queue.append(v)
                visit[v] = True
                parent[v] = u
                if(v == d):
                    return True
    return False


print (fordful(g, 0, 5))
