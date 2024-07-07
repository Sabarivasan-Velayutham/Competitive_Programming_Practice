
# leetcode link  :
# https://leetcode.com/problems/can-i-win/


# Two players take turns drawing from a common pool of numbers of 1..15 without replacement 
# until they reach a total ≥ 100.

# Given an integer maxChoosableInt and another integer desiredTotal, determine if the 
# first player to move can force a win, assuming both players play optimally.

# You can always assume that maxChoosableInt will not be larger than 20 and 
# desiredTotal will not be larger than 300. Below is an example explanation.

# Input:
# maxChoosableInteger = 10
# desiredTotal = 11

# Output:
# false

# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
# Same with other integers chosen by the first player, the second player will always win.


class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if maxChoosableInteger >= desiredTotal:
            return True
        if (maxChoosableInteger + 1) * maxChoosableInteger // 2 < desiredTotal:
            return False

        # Create a dictionary to memoize the results of subproblems
        memo = {}

        # Define the recursive function to determine if the first player can force a win
        def canWin(maxChoosableInteger, desiredTotal, used):
            if used in memo:
                return memo[used]

            for i in range(1, maxChoosableInteger + 1):
                mask = 1 << (i - 1)
                if not (used & mask):
                    if i >= desiredTotal or not canWin(maxChoosableInteger, desiredTotal - i, used | mask):
                        memo[used] = True
                        return True

            memo[used] = False
            return False

        # Start with no numbers used and check if the first player can win
        return canWin(maxChoosableInteger, desiredTotal, 0)
        
