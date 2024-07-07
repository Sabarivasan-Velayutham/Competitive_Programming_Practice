
# You are given an array A of length N, which initially contains of only 1 's:
# We call the subarray from L to R good, if for all pairs of elements in this range have product as a perfect square.
# You are also given a 2D array Queries which consists of Q queries. Each query is one of the two
# types:
# • Type 1 - 1 L R: Replace A[L] with R.
# • Type 2 - 2 L R: Find the length of the longest good subarray contained in the range from L to R.

# Find the bitwise XOR of all queries of Type 2. Since the answer can be very large, return it modulo 10^9+7.


# The first line contains an integer, N, denoting the size of array A.
# The next line contains an integer, Q denoting the number of rows in Queries.
# The next line contains an integer Col, denoting the number of columns in Queries.
# Each line i of the Q subsequent lines (where 0 <= i < Q) contains Col space separated integers each
# describing the row Queries[i).


# ================

# case 1
# Input:
# 5
# 5
# 3
# 2 1 3
# 2 1 1
# 1 1 1
# 1 1 2
# 2 2 2

# Output: 3

# explanation :
# Given N 5, Q 5,
# After 1st Query A [1, 1, 1, 1, 1], then length of longest good subarray in range [1, 3 ] is equal to 3.
# After 2nd Query A  [1, 1, 1, 1, 1], the length of the longest good subarray in range [1, 1] is equal 1
# After 3rd Query A [1, 1, 1, 1, 1]
# After 4th Query A [1, 1, 1, 1, 1]
# After 5th Query A [2, 1, 1, 1, 1], the length of the longest good subarray in range [2, 2] is 1

# The bitwise XOR of answers of queries of type 2 is equal to 3 XOR 1 XOR 1 = 3

# ===============

# case 2
# Input:
# 5
# 5
# 3
# 2 1 3
# 2 1 1
# 1 1 64
# 1 2 64
# 2 1 5

# Output: 7

# explanation :

# Given N 5, Q 5,
# After 1st Query A [1, 1, 1, 1, 1], then length of longest good subarray in range [1, 3 ] is equal to 3.
# After 2nd Query A  [1, 1, 1, 1, 1], the length of the longest good subarray in range [1, 1] is equal 1
# After 3rd Query A [64, 1, 1, 1, 1]
# After 4th Query A [64, 64, 1, 1, 1]
# After 5th Query A [64, 64, 1, 1, 1], the length of the longest good subarray in range [1, 5] is 5

# The bitwise XOR of answers of queries of type 2 is equal to 3 XOR 1 XOR 5 = 7

# ======================

# case 3
# Input:
# 5
# 5
# 3
# 1 1 2
# 1 3 2
# 2 1 3
# 2 1 2
# 2 2 3

# Output: 1


# explanation :

# N 3 Q 5
# After the first 2 queries, • the array is [2, 1, 2], and the answers are: 1, 1, 1 and their xor is 1.

# =====================
# write the python code to solev this problem
# def get_ans(N, Q, Col, Queries):
#     #Write your code here


from collections import defaultdict
from math import isqrt

MOD = 10**9 + 7


def pf(n):
    f = defaultdict(int)
    for i in range(2, isqrt(n) + 1):
        while n % i == 0:
            f[i] += 1
            n //= i
    if n > 1:
        f[n] += 1
    return f


def merge_f(f1, f2):
    for p, c in f2.items():
        f1[p] += c
    return f1


def build_seg(A, seg, s, e, n):
    if s == e:
        seg[n] = pf(A[s])
        return seg[n]

    mid = (s + e) // 2
    left = build_seg(A, seg, s, mid, 2 * n + 1)
    right = build_seg(A, seg, mid + 1, e, 2 * n + 2)
    seg[n] = merge_f(left, right)
    return seg[n]


def update_seg(A, seg, s, e, idx, val, n):
    if s == e:
        A[idx] = val
        seg[n] = pf(A[s])
        return seg[n]

    mid = (s + e) // 2
    if s <= idx <= mid:
        left = update_seg(A, seg, s, mid, idx, val, 2 * n + 1)
        right = seg[2 * n + 2]
    else:
        left = seg[2 * n + 1]
        right = update_seg(A, seg, mid + 1, e, idx, val, 2 * n + 2)

    seg[n] = merge_f(left, right)
    return seg[n]


def query_seg(seg, s, e, L, R, n):
    if R < s or e < L:
        return defaultdict(int)
    if L <= s and e <= R:
        return seg[n]

    mid = (s + e) // 2
    left = query_seg(seg, s, mid, L, R, 2 * n + 1)
    right = query_seg(seg, mid + 1, e, L, R, 2 * n + 2)
    return merge_f(left, right)


def is_good(f):
    for c in f.values():
        if c % 2 != 0:
            return False
    return True


def get_ans(N, Q, C, Qs):
    A = [1] * N
    seg = [defaultdict(int) for _ in range(4 * N)]

    build_seg(A, seg, 0, N - 1, 0)
    xor_res = 0

    for q in Qs:
        if q[0] == 1:
            _, L, R = q
            update_seg(A, seg, 0, N - 1, L - 1, R, 0)
        elif q[0] == 2:
            _, L, R = q
            f = query_seg(seg, 0, N - 1, L - 1, R - 1, 0)
            max_len = 0
            start = L - 1
            cur_f = defaultdict(int)
            for end in range(L - 1, R):
                cur_f = merge_f(cur_f, pf(A[end]))
                while not is_good(cur_f) and start <= end:
                    for p, c in pf(A[start]).items():
                        cur_f[p] -= c
                    start += 1
                max_len = max(max_len, end - start + 1)
            xor_res ^= max_len
            xor_res %= MOD

    return xor_res


# Example usage
N1 = 5
Q1 = 5
C1 = 3
Qs1 = [
    [2, 1, 3],
    [2, 1, 1],
    [1, 1, 1],
    [1, 1, 2],
    [2, 2, 2]
]
print(get_ans(N1, Q1, C1, Qs1))  # Output: 3

N2 = 5
Q2 = 5
C2 = 3
Qs2 = [
    [2, 1, 3],
    [2, 1, 1],
    [1, 1, 64],
    [1, 2, 64],
    [2, 1, 5]
]
print(get_ans(N2, Q2, C2, Qs2))  # Output: 7

N3 = 3
Q3 = 5
C3 = 3
Qs3 = [
    [1, 1, 2],
    [1, 3, 2],
    [2, 1, 3],
    [2, 1, 2],
    [2, 2, 3]
]
print(get_ans(N3, Q3, C3, Qs3))  # Output: 1
