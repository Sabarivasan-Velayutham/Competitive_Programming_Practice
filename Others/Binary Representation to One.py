

# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/

class Solution(object):
    def numSteps(self, s):
        num = int(s)
        dec = 0
        i = 0
        while(num != 1):
            last = num % 10
            num = num / 10
            dec = dec + last * 2**i
            i = i+1
        count = 0
        while(dec != 1):
            if(dec % 2 != 0):
                dec = dec + 1
                count = count + 1
            elif(dec % 2 == 0):
                dec = dec // 2
                count = count + 1
        return count
