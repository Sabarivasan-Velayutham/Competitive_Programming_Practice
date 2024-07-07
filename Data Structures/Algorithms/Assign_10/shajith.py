
def bfs(rG,s,d,p):
    vis = [0]*len(p)
    q = []
    q.append(s)
    vis[s] = 1
    p[s] = -1
    while q:
        u = q.pop(0)
        # for v in range(len(p)):
        #     if(vis[v]==0 and rG[u][v]):
        #         if v==d:
        #             p[v] = u
        #             vis[v] = 1
        #             return True
        #     q.append(v)
        #     vis[v] = 1
        #     p[v] = u
        for v in range(len(p)):
            if(vis[v]==0 and rG[u][v]):
                q.append(v)
                vis[v] = 1
                p[v] = u
                if v==d:
                    return True
            
    return False

def fordFulkerson(rG,s,d):
    p = [0]*(len(rG[0]))
    mxFlow = 0
    while bfs(rG,s,d,p):
        pFlow = 99999
        v = d
        while v!=s:
            pFlow = min(pFlow,rG[p[v]][v])
            v = p[v]
            v = d
        while v!=s:
            rG[p[v]][v]-=pFlow
            rG[v][p[v]]+=pFlow
            v = p[v]
            mxFlow+=pFlow
    return mxFlow

e = int(input("Enter the no of edges:"))
print("Enter the Adjacency Matrix:")
print()
graph = []
for i in range(e):
    graph.append(list(map(int,input().split())))
print("The Max Flow is :",fordFulkerson(graph,0,5))