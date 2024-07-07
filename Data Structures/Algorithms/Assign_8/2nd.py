

def floydWarshall(graph):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    printSolution(graph)


def printSolution(dist):
    for i in dist:
        print(i)


graph = []
V = int(input())
# INF = 99999
print("enter 9999 if no edge is present")
for i in range(V):
    arr = list(map(int, input().split()))
    graph.append(arr)
floydWarshall(graph)

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
