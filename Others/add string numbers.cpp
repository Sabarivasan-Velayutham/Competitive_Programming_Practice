

// https://leetcode.com/problems/add-strings/description/

// https://leetcode.com/problems/add-strings/solutions/2808140/c-grade-1-addition-technique/

class Solution
{
public:
    string addStrings(string num1, string num2)
    {
        string ans;
        reverse(num1.begin(), num1.end());
        reverse(num2.begin(), num2.end());

        int i = 0, j = 0, carry = 0;
        while (i < num1.size() or j < num2.size() or carry)
        {
            int sum = 0;
            if (i < num1.size())
                sum += num1[i++] - '0';
            if (j < num2.size())
                sum += num2[j++] - '0';

            sum += carry;
            ans += to_string(sum % 10);
            carry = sum / 10;
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};