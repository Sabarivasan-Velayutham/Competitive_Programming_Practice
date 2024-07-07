

# https://leetcode.com/problems/count-sorted-vowel-strings/description/

# https://leetcode.com/problems/count-sorted-vowel-strings/solutions/1021273/python-one-liner-solution-o-1-time-space/


class Solution:
    def countVowelStrings(self, n):
        return ((n + 1) * (n + 2) * (n + 3) * (n + 4))//24
