

# https://leetcode.com/problems/vowels-of-all-substrings/description/

# https://leetcode.com/problems/vowels-of-all-substrings/solutions/2001779/python-combinatrics-math/

class Solution(object):
    def countVowels(self, word):
        vowels = {'a','e','i','o','u'}
        count = 0 
        leng = len(word)
        for i in range(leng):
            if word[i] in vowels:
                left = i + 1
                right = leng - i
                count += left*right
        return count