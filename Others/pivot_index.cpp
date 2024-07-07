

// https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1

#include <vector>

class Solution
{
public:
    int pivotIndex(vector<int> &nums)
    {
        int leftarray[10000];
        int rightarray[10000];
        int leftsum = 0, rightsum = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            leftsum += nums[i];
            leftarray[i] = leftsum;
        }
        for (int i = nums.size() - 1; i >= 0; i--)
        {
            rightsum += nums[i];
            rightarray[i] = rightsum;
        }
        for (int i = 0; i < nums.size(); i++)
        {
            if (leftarray[i] == rightarray[i])
                return i;
        }
        return -1;
    }
};