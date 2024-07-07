

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/2040282/o-n-time-beats-99-97-memory-speed-0ms-may-2022/

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int profit = 0;
        int mini = INT_MAX;

        for (int i = 0; i < prices.size(); i++)
        {
            mini = min(mini, prices[i]);
            profit = max(profit, prices[i] - mini);
        }

        return profit;
    }
};