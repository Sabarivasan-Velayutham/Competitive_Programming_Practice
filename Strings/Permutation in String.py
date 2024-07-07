

# https://leetcode.com/problems/permutation-in-string/description/

# https://leetcode.com/problems/permutation-in-string/solutions/3138596/leetcode-the-hard-way-explained-line-by-line-sliding-window/
# https://www.youtube.com/watch?v=XFh_AoEdOTw

class Solution(object):
    def checkInclusion(self, s1, s2):
        
        if len(s1)>len(s2):
            return False
        
        freq_s1 = [0]*26
        freq_s2 = [0]*26

        # to find freq of letters in s1
        for i in range(len(s1)):
            freq_s1[ord(s1[i])-ord('a')] += 1

        for j in range(len(s2)):
            freq_s2[ord(s2[j])-ord('a')] += 1

            # sliding window 
            if j>=len(s1):
                freq_s2[ord(s2[j-len(s1)])-ord('a')] -= 1
            if freq_s1 == freq_s2:
                return True
        return False 