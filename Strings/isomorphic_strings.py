
# https://leetcode.com/problems/isomorphic-strings/description/

class Solution(object):
    def isIsomorphic(self, s, t):
        hashmap = dict()
        for i in range(len(s)) :
            if s[i] not in hashmap:
                if t[i] in hashmap.values():
                    return False 
                hashmap[s[i]] = t[i]
            elif t[i] != hashmap[s[i]]:
                return False 
        return True
