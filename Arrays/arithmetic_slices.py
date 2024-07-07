

# https://leetcode.com/problems/arithmetic-slices/

# https://leetcode.com/problems/arithmetic-slices/solutions/982169/faster-than-99-44-python-3-simple-solution/


class Solution:
    def numberOfArithmeticSlices(self, A):
        le = len(A)
        l = [0]*(le)
        for i in range(2, le):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                l[i] = 1+l[i-1]
        return sum(l)
