


// https://leetcode.com/problems/partition-equal-subset-sum/description/

// explanation
// https://leetcode.com/problems/partition-equal-subset-sum/solutions/1624365/c-easy-to-solve-beginner-friendly-detailed-explanation-with-a-dry-run/
// https://youtu.be/obhWqDfzwQQ

class Solution
{
public:
    bool canPartition(vector<int> &nums)
    {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % 2 == 1)
            return false;

        int half_sum = sum / 2;

        // dp vector for storing the results of previous row
        //  dp will keep for each number if it has a satisfying subset or not
        vector<bool> dp(half_sum + 1, false);
        dp[0] = true;
        for (auto x : nums)
        {
            for (int i = half_sum; i >= x; i--)
                dp[i] = dp[i] || dp[i - x];
        }
        return dp[half_sum];
    }
};