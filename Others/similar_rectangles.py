

# https://www.geeksforgeeks.org/count-pairs-of-similar-rectangles-possible-from-a-given-array/

from collections import defaultdict

sides = [[4, 8], [10, 20], [15, 30], [3, 6]]
count = 0 
hashmap = defaultdict(int)

for i in sides :
    ratio = i[0]/i[1]
    hashmap[ratio] += 1 

for i in hashmap:
    results = hashmap[i]
    count += results*(results-1)/2

print(int(count))