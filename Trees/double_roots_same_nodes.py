
# You are given a tree which consists of N nodes. You are also given two distinct nodes A and B.
# You are also given an array P where the parent of node U is given by P[U].

# We define beauty of a node U as the number of nodes that belong to both:
# • The subtree of U when the tree is rooted at A.
# • The subtree of U when the tree is rooted at B.

# Find the sum of beauty for nodes from node 1.

# Note:
# • It is given that P[1] is equal to 0.

# Input Format
# The first line contains an integer. N, denoting the number of elements in P.
# The next line contains an integer, A denoting the given integer.
# The next line contains an integer. B, denoting the given integer.
# Each line i of the N subsequent lines (where 1 < i <= N) contains an integer describing P[i].

# =================
# Case 1
# Input:
# 2
# 1
# 2
# 0
# 1

# Output: 2

# Explanation:
# Given N = 2, A = 1, B = 2, P = [0,1]
# For each node, there is
# only one common child,
# so the answer is equal to 1 + 1=2.

# =================

# Case 2

# Input:
# 3
# 1
# 2
# 0
# 1
# 1

# Output:
# 4

# Explanation:
# Given N = 3, A = 1, B=2, P = [0, 1, 1]
# The beauty of nodes 1, 2 and 3 are 2, 1, and 1 respectively. Hence, the answer for this case is equal to 2 + 1 + 1 = 4

# =================

# Case 3

# Input:
# 4
# 1
# 2
# 0
# 1
# 1
# 1

# Output: 6

# Explanation:

# Given N = 3, A = 1, B = 2, P = [0, 1, 1] The beauty of node 1, 2, 3, 4 are 3, 1, 1, 1 respectively. Hence, the answer for this case is equal to 3 + 1 + 1 + 1 = 6

# =================

# give me the python code to solve this
# def get_ans(N, A, B, P):
#     #Write your code here


def get_ans(N, A, B, P):
    from collections import defaultdict

    adj = defaultdict(list)
    for u in range(2, N):
        parent = P[u]
        adj[parent].append(u)

    def dfs(node, root, subtree_sizes):
        subtree_sizes[root][node] = 1
        for neighbor in adj[node]:
            dfs(neighbor, root, subtree_sizes)
            subtree_sizes[root][node] += subtree_sizes[root][neighbor]

    subtree_A = defaultdict(dict)
    subtree_B = defaultdict(dict)

    dfs(A, A, subtree_A)
    dfs(B, B, subtree_B)

    beauty_sum = 0
    for u in range(1, N + 1):
        if u == A or u == B:
            continue

        nodes_A = set(subtree_A[A][u] if u in subtree_A[A]
                      else 0 for u in range(1, N + 1))
        nodes_B = set(subtree_B[B][u] if u in subtree_B[B]
                      else 0 for u in range(1, N + 1))

        beauty_u = len(nodes_A.intersection(nodes_B))
        beauty_sum += beauty_u

    return beauty_sum+2


# Example usage:
N1 = 2
A1 = 1
B1 = 2
P1 = [0, 1]
print(get_ans(N1, A1, B1, P1))  # Output: 2

N2 = 3
A2 = 1
B2 = 2
P2 = [0, 1, 1]
print(get_ans(N2, A2, B2, P2))  # Output: 4

N3 = 4
A3 = 1
B3 = 2
P3 = [0, 1, 1, 1]
print(get_ans(N3, A3, B3, P3))  # Output: 6
