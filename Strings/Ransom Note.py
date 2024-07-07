

# https://leetcode.com/problems/ransom-note/description/

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        d = dict()
        for i in magazine:
            if i not in d:
                d[i] = 1
            else :
                d[i] += 1

        for i in ransomNote:
            if i not in d :
                return False
            elif i in d and d[i]==0 :
                return False 
            else :
                d[i] -= 1
        
        return True
        
        
