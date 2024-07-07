

// https://leetcode.com/problems/subarray-sum-equals-k/


// https://leetcode.com/problems/subarray-sum-equals-k/solutions/1532651/c-explained-code-using-hashmap-with-time-complexity-analysis/
// https://youtu.be/HbbYPQc-Oo4
// https://gist.github.com/SuryaPratapK/cc99cf19e8d65a96525ee1c87d3e75c7


// for find func of unordered map (why usage of end())
// https://www.geeksforgeeks.org/map-find-function-in-c-stl/



class Solution
{
public:
    int subarraySum(vector<int> &nums, int k)
    {
        int len = nums.size();
        unordered_map<int, int> mymap; // Key = PrefixSUM, Value = Count of PrefixSUM.
        int sum = 0, count = 0;

        for (int i = 0; i < len; i++)
        {
            sum += nums[i];
            if (sum == k)
                count++;
            if (mymap.find(sum - k) != mymap.end())
                count += mymap[sum - k];

            mymap[sum]++;
        }
        return count;
    }
};