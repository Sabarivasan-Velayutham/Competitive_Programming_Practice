
# The task is to count all the possible paths from top left to bottom right of a m x n matrix
# with the constraints that from each cell you can either move only to right or down.


# Input:
# First line of every test case consists of N and M, denoting the number of rows and number
# of columns respectively.

# Output:
# Single line output i.e count of all the possible paths from top left to bottom right of a
# m x n matrix..

# Input:
# 2 2

# Output:
# 2

# Explanation:

# There are two paths

# (0, 0) -> (0, 1) -> (1, 1)

# (0, 0) -> (1, 0) -> (1, 1)


def numberOfPaths(m, n):
    # If either given row number is first
    # or given column number is first
    if (m == 1 or n == 1):
        return 1

# If diagonal movements are allowed
# then the last addition
# is required.
    return numberOfPaths(m-1, n) + numberOfPaths(m, n-1)


m, n = list(map(int, input().split()))
print(numberOfPaths(m, n))
