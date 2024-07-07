


// https://leetcode.com/problems/multiply-strings/description/

// explanation
// https://youtu.be/1vZswirL8Y8

// https://leetcode.com/problems/multiply-strings/solutions/1476451/simple-c-solution-faster-than-95-with-proper-comments-dry-run-beginner-friendly/


class Solution
{
public:
    string multiply(string num1, string num2)
    {
        if (num1 == "0" or num2 == "0")
            return "0";

        int s1 = num1.size() - 1;
        int s2 = num2.size() - 1;
        vector<int> ans(s1 + s2 + 2);

        reverse(num1.begin(), num1.end());
        reverse(num2.begin(), num2.end());

        for (int i = 0; i <= s1; i++)
        {
            for (int j = 0; j <= s2; j++)
            {
                int digit = (num1[i] - '0') * (num2[j] - '0');
                ans[i + j] += digit;
                ans[i + j + 1] += (ans[i + j]) / 10;
                ans[i + j] = (ans[i + j]) % 10;
            }
        }
        reverse(ans.begin(), ans.end());
        int k = 0;

        // remove the starting zeroes
        while (k < ans.size() and ans[k] == 0)
            k++;

        // convert vector to string
        string result;
        while (k < ans.size())
        {
            result += (ans[k] + '0');
            k++;
        }
        return result;
    }
};
