

# https://leetcode.com/problems/merge-intervals/description/

# https://www.youtube.com/watch?v=2JzRBPFYbKE

class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        ans = []
        intervals.sort()
        print(intervals)

        tmp = intervals[0]
        for i in range(1, len(intervals)):
            if tmp[1] >= intervals[i][0]:
                tmp[1] = max(tmp[1], intervals[i][1])
            else:
                ans.append(tmp)
                tmp = intervals[i]
        ans.append(tmp)
        return ans
