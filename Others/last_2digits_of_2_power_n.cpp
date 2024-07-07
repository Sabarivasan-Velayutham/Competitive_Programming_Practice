

#include <iostream>
using namespace std;

/* Iterative Function to calculate (x^y)%p in O(log y) */
int power(long long int x, long long int y, long long int p)
{
    long long int res = 1; // Initialize result

    x = x % p; // Update x if it is more than or equal to p

    while (y > 0)
    {

        // If y is odd, multiply x with result
        if (y % 2 == 1)
            res = (res * x) % p;

        // y must be even now
        y = y / 2;
        x = (x * x) % p;
    }
    return res;
}

int numberOfDigits(int x)
{
    int i = 0;
    while (x)
    {
        x /= 10;
        i++;
    }
    return i;
}

int main()
{
    int n = 987456;
    cout << "Last " << 2;
    cout << " digits of " << 2;
    cout << "^" << n << " = ";

    int tmp = 100;
    // Calling modular exponentiation
    cout << power(2, n, tmp);
}
