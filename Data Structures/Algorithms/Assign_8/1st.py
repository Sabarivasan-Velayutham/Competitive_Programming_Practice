n = int(input())
wt = list(map(int,input().split()))
val = list(map(int,input().split()))
w = int(input())

dp = [[0 for i in range(w+1)] for j in range(n+1)]
# print(dp)

def ks(w,wt,val,n):
    if n==0 or w==0:
        return 0
    if dp[n][w]:
        return dp[n][w]
    if wt[n-1]<=w:
        dp[n][w] = max(val[n-1]+ks(w-wt[n-1],wt,val,n-1),ks(w,wt,val,n-1))
    else:
        dp[n][w] = ks(w,wt,val,n-1)
    return dp[n][w]

print('max value:',ks(w,wt,val,n))

# for i in dp:
#     print(*i)

def ele():
    global w
    res = dp[n][w]
    W = w
    picked = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == dp[i - 1][W]:
            continue
        else:
            picked.append(wt[i - 1])
            res = res - val[i - 1]
            W = W - wt[i - 1]
    print("Weigths : ",*picked)
    
ele()

# 3
# 10 20 30 
# 60 100 120
# 50

# max value: 220
# Weigths :  30 20