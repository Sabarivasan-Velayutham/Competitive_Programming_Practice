
// https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution
{
public:
    int Search(vector<int> &v, int low, int high, int target)
    {
        int middle, min1 = -1, min2 = -1;
        if (low < high)
        {
            middle = (low + high) / 2;
            min1 = Search(v, low, middle, target);
            min2 = Search(v, middle + 1, high, target);
            if (min1 >= min2)
            {
                return min1;
            }
            return min2;
        }
        if (v[low] == target)
        {
            return low;
        }
        return -1;
    }

    int search(vector<int> &nums, int target)
    {
        return Search(nums, 0, nums.size() - 1, target);
    }
};
