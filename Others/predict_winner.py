

# https://leetcode.com/problems/predict-the-winner/solutions/746142/easy-python-100-speed-recursion-memoization/

class Solution:
    def predictTheWinner(self, nums):
        memo = {}

        def maxscore(i, j):
            if (i, j) in memo:
                return memo[i, j]
            if i > j:
                return 0

            # pick nums[i] + min of the 2 possible upcoming turns (player 2 is smart)
            sA = nums[i] + min(maxscore(i+1, j-1), maxscore(i+2, j))
            sB = nums[j] + min(maxscore(i, j-2), maxscore(i+1, j-1))
            score = max(sA, sB)
            memo[i, j] = score
            return score

        # calling maxscore funs
        p1 = maxscore(0, len(nums)-1)  # Score Player 1
        return p1 >= (sum(nums)-p1)  # p1 >= p2
