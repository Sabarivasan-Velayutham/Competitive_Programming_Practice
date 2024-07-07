
def bfs(g,s,d,p):
    vis=[0]*len(g)
    q=[]
    p[s]=-1
    vis[s]=1
    q.append(s)

    while q :
        u = q.pop(0)
        for v in range(len(p)):
            if vis[v]==0 and g[u][v]:
                q.append(v)
                vis[v]=1
                p[v]=u
                if v == d:
                    return True
    return False

def ford(g,s,d):
    p = [0]*len(g)
    maxflow = 0
    while (bfs(g,s,d,p)):
        pathflow = 9999

        temp1 = d       
        while temp1 != s :
            u = p[temp1]
            pathflow = min(pathflow,g[u][temp1])
            temp1 = p[temp1]

        maxflow+=pathflow

        temp2 = d
        while temp2 != s :
            u = p[temp2]
            g[u][temp2]-=pathflow
            g[temp2][temp2]+=pathflow
            temp2 = p[temp2]

    return maxflow



g=[]
for i in range(6):
    g.append(list(map(int,input().split())))
print("max flow : ",ford(g,0,5))