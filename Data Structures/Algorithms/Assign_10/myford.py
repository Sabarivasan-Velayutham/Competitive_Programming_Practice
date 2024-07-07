
def bfs(graph,sourse,destination,parent):
    visited = [0]*len(graph)
    # print(visited)
    q = []
    q.append(sourse)
    visited[sourse] = 1
    parent[sourse] = -1
    while q:
        u = q.pop(0)

        for v in range(len(parent)):
            if(visited[v]==0 and graph[u][v]) :
                q.append(v)
                visited[v] = 1
                parent[v] = u
                if v==destination:
                    return True
            
    return False


def fordFulkerson(graph,source,destination):
    parent = [0]*(len(graph))
    mxFlow = 0
    while bfs(graph,source,destination,parent):
        pFlow = 99999
        temp_dest = destination
        while temp_dest!=source:
            u = parent[temp_dest]
            pFlow = min(pFlow,graph[u][temp_dest])
            temp_dest = parent[temp_dest]
        mxFlow+=pFlow

        temp_dest_2 = destination

        # update residual capacities of the edges and reverse edges
        # along the path
        while temp_dest_2!=source:
            u = parent[temp_dest_2]
            graph[u][temp_dest_2]-=pFlow
            graph[temp_dest_2][temp_dest_2]+=pFlow
            temp_dest_2 = parent[temp_dest_2]
            
    return mxFlow

e = int(input("Enter the no of edges:"))
print("Enter the Adjacency Matrix:")
print()
graph = []
for i in range(e):
    graph.append(list(map(int,input().split())))
print("The Max Flow is : ",fordFulkerson(graph,0,5))


# 0 16 13 0 0 0
# 0 0 10 12 0 0
# 0 4 0 0 14 0
# 0 0 9 0 0 20
# 0 0 0 7 0 4
# 0 0 0 0 0 0