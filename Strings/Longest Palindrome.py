

# https://leetcode.com/problems/longest-palindrome/description/

# https://leetcode.com/problems/longest-palindrome/solutions/791646/c-python-java-it-is-only-easy-when-you-think-really-hard-to-spot-the-built-in-nature/

class Solution(object):
    def longestPalindrome(self, s):
        d = dict()
        ans = 0
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        flag = False
        for i in d.values():
            if i % 2 == 1:
                flag = True
                ans += i-1
            else:
                ans += i

        if flag:
            return ans + 1
        return ans
