


// https://leetcode.com/problems/move-zeroes/description/

// https://leetcode.com/problems/move-zeroes/solutions/2460373/c-100-two-pointer-single-loop-o-n-solution/


class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0 , j = 0 ;
        int len  = nums.size();
        while (i<len and j<len)
        {
            if ( nums[j] != 0 )
            {
                swap(nums[i],nums[j]);
                i++;
                j++;
            }
            else j++;
        }
    }
};