class Solution
{
public:
    int squares(int num)
    {
        int sum = 0;
        while (num > 0)
        {
            int last = num % 10;
            sum += last * last;
            num /= 10;
        }
        return sum;
    }

    bool isHappy(int n)
    {
        if (n == 1 or n == 7)
            return true;
        if (n < 10)
            return false;
        return isHappy(squares(n));
    }
};