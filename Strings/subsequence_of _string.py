
# iterative time O(n) space O(1)
# https://www.geeksforgeeks.org/given-two-strings-find-first-string-subsequence-second/

# using stack -> time and space O(n)
# https://www.geeksforgeeks.org/check-if-a-string-is-a-subsequence-of-another-string-using-stacks/


# using stack method
print("Stack method ...")
mainstring = "afbef"
stack = list("ab")
top = len(stack)-1
flag = 0

for i in range(len(mainstring)-1, -2, -1):
    if top == -1:
        flag = 1
        print("YES")
        break
    if stack[top] == mainstring[i]:
        stack.pop()
        top -= 1

if flag == 0:
    print("NO")


# using iterative method
print("Iterative method ...")
mainstring = "sabarivasan"
target = "aariaan"

i, j = 0, 0
while (i < len(mainstring) and j < len(target)):
    if mainstring[i] == target[j]:
        j += 1
    i += 1

if j == len(target):
    print("YES")
else:
    print("NO")


# find the length of the smallest prefix of S which is not a subsequence of T
# if nothing exists return -1

# S="abbbb"
# T = "afbef"
# return 3
# "abb" is prefix of S but not a
# Subsequence of T.


# S="a"
# T = "afdcf"
# return -1
# Every prefix of S is a subsequence
# of T.


print("Geeks for Geeks ... ")
# https://practice.geeksforgeeks.org/contest/gfg-weekly-coding-contest-85/problems/


# GFGS SOLUTION
class Solution:
    def maximumPrefix(self, n, m, target, mainstring):
        i, j, count = 0, 0, 1
        while(i < n and j < m):
            if (target[i] == mainstring[j]):
                i += 1
                count += 1
            j += 1
        if count == n+1:
            return -1
        return count
