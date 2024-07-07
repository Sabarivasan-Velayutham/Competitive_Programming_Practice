
# tutorial
# https://www.youtube.com/watch?v=qtVh-XEpsJo
# https://www.youtube.com/watch?v=RqxIXM6eyiY

# code
# https://www.youtube.com/watch?v=wiGpQwVHdE0


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans = 0
        left = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            ans = max(ans, right-left+1)

        return ans
