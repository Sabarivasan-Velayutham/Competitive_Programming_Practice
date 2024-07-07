
# 1685. Sum of Absolute Differences in a Sorted Array
# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/description/

# solution 
# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/solutions/2954667/python-solution-with-explaination-and-comments/

class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        ans = []
        length = len(nums)
        total = sum(nums)
        prefix_sum = 0 

        for i in range(length):
            prefix_sum += nums[i]
            left_count = i
            right_count = length-i-1

            rightside = total - prefix_sum - nums[i]*right_count
            leftside = nums[i]*(left_count+1)- prefix_sum
            ans.append(leftside + rightside)

        return ans 
