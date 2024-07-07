


# https://leetcode.com/problems/two-sum/description/

# https://leetcode.com/problems/two-sum/solutions/737092/sum-megapost-python3-solution-with-a-detailed-explanation/


class Solution(object):
    def twoSum(self, nums, target):
        d = dict()
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in d:
                return [d[rem], i]
            else:
                d[nums[i]] = i
