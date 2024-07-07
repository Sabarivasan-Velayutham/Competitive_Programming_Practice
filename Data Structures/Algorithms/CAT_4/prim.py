

def prim(g,v):
    selected=[0,0,0,0,0]
    selected[0] = True
    edges = 0 

    while ( edges < v-1):
        x=0
        y=0
        minimum = 999999
        for i in range(v):
            if selected[i]:
                for j in range(v):
                    if not selected[j] and g[i][j]: 
                        if minimum > g[i][j]:
                            minimum = g[i][j]
                            x=i
                            y=j
        print(chr(65+x) + " : " + chr(65+y) + " -> "+str(g[x][y]))
        selected[y]=True
        edges+=1

# number of vertices in graph
V = 5

# create a 2d array of size 5x5
# for adjacency matrix to represent graph
G = [[0, 4, 0, 3, 5],
     [4, 0, 2, 0, 0],
     [0, 2, 0, 1, 0],
     [3, 0, 1, 0, 0],
     [5, 0, 0, 0, 0]]

prim(G,V)
