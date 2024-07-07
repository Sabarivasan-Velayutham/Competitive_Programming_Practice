

// exlpanation.
// https://youtu.be/ZUt8L8cbbBI

// question
// https://leetcode.com/problems/add-binary/description/

class Solution
{
public:
    string addBinary(string a, string b)
    {
        string result = "";
        int carry = 0;
        int i = a.size() - 1;
        int j = b.size() - 1;

        int sum;
        while (i >= 0 or j >= 0)
        {
            sum = carry;
            // sum =  1 - 0; 0 - 0  ;
            if (i >= 0)
                sum += a[i] - '0';
            if (j >= 0)
                sum += b[j] - '0';

            // 0%2=0 and 1%2=1 with no carry ; 2%2=0 with carry 1
            result += to_string(sum % 2);
            carry = sum / 2;

            i--;
            j--;
        }
        if (carry != 0)
            result += '1';

        reverse(result.begin(), result.end());
        return result;
    }
};
