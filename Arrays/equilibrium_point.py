
# You are given an array A of size N.
# An equilibrium point is an index in A such that the sum of elements to the left of that index is
# equal to the sum of elements to the right of that index.
# Find the total number of equilibrium points in A.


# Input Format
# The first line contains an integer, N. denoting the number of elements in A.
# Each line i of the N subsequent lines (where 0 < i <= N) contains an integer describing A[i].

# input 
# 5
# 1
# 1
# 1
# 1
# 2

# output : 0

# Explanation:
# Given N - 5, A - [1, 1, 1, 1, 2]
# There does not exist any equilibrium points in the given array, so the answer is 0.



def solve(N, A):
    total_sum = sum(A)
    left_sum = 0
    equilibrium_count = 0

    for i in range(N):
        total_sum -= A[i]

        if left_sum == total_sum:
            equilibrium_count += 1

        left_sum += A[i]

    return equilibrium_count


N = 5
A = [1, 1, 1, 1, 2]
print(solve(N, A))  # Output: 0

N = 5
A = [3, -1, 0, 2, 0]
print(solve(N, A))  # Output: 1

N = 5
A = [2, -1, 0, 0, 1]
print(solve(N, A))  # Output: 3
