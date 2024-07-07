
def floyd(graph):
    for k in range(4):
        for i in range(4):
            for j in range(4):
                graph[i][j] = min( graph[i][j], graph[i][k] + graph[k][j] )
    for i in graph:
        print(i)

v=4
graph=[]
for i in range(v):
    graph.append(list(map(int,input().split())))
print(graph)
floyd(graph)

# 4
# enter 9999 if no edge is present
# 0 3 9999 5
# 2 0 9999 4
# 9999 1 0 9999
# 9999 9999 2 0

# [0, 3, 7, 5]
# [2, 0, 6, 4]
# [3, 1, 0, 5]
# [5, 3, 2, 0]
