# 2) Implement Greedy solution for the
# Knapsack problem 

from itertools import combinations as c

capacity  = 100
weigths = [10, 15, 35, 45]
possibilities = []
best = 0
flag = 0 

for i in range(len(weigths)) : 
    comb = c(weigths,i+1)
    for i in comb :
        if sum(i) <= capacity:
            best = max(best,sum(i))
            if best == capacity:
                print("Solution : ")
                print(i)
                flag = 1 
                break
            possibilities.append(i)
    if flag ==  1 :
        break 

if flag == 0 :    
    print(possibilities)
    print("Solution : ")
    print(best)
