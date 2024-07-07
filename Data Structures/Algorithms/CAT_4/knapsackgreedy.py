
# from itertools import combinations as c

# capacity  = 100
# weigths = [10, 15, 35, 45]
# best = 0
# flag=0

# for i in range(4):
#     comb = c(weigths,i+1)
#     for j in comb :
#         print(j,end='')
#         if sum == capacity :
#             print(sum)
#             flag=1
#             break

#         if sum(j)<capacity:
#             best = max(best,sum(j))

# if flag==0:
#     print(best)


def knapsack(value, weight, capacity):

    fractions = [0]*len(value)
    max_value = 0

    index = [i for i in range(len(value))]
    print(index)

    ratio = [v/w for v, w in zip(value, weight)]
    print(ratio)

    index.sort(key=lambda i: ratio[i], reverse=True)
    print(index)

    for i in index:
        if weight[i] < capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            max_value += value[i]*fractions[i]
            break

    return max_value, fractions


n = 5
value = [2, 5, 1, 3, 4]
weight = [25, 15, 50, 30, 40]
capacity = 100

max_value, fractions = knapsack(value, weight, capacity)
print('Maximum value of items : ', max_value)
print('Fractions : ', fractions)
