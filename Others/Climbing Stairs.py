

# https://leetcode.com/problems/climbing-stairs/description/

# https://leetcode.com/problems/climbing-stairs/solutions/1792723/python-in-depth-walkthrough-explanation-dp-top-down-bottom-up/

class Solution(object):
    def climbStairs(self, n):
        d = dict()
        # base case
        d = {1: 1, 2: 2}

        def climb(n):
            if n in d:
                return d[n]
            else:
                d[n] = climb(n-1) + climb(n-2)
                return d[n]
        return climb(n)


# c++ code 
# https://leetcode.com/problems/climbing-stairs/solutions/1428533/3-lines-code-faster-than-100-beginner-friendly-detailed-explanation-of-approach/
'''
class Solution {
public:
    int dp[46] ;
    int climbStairs(int n) {
        if(n==1 || n==2) return n;
        if ( dp[n] != 0 ) return dp[n];
        dp[n] = climbStairs(n-1) + climbStairs(n-2) ;
        return dp[n] ;
    }
};
'''
