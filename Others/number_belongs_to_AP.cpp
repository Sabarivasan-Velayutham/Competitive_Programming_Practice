

// To solve this problem, we will follow these steps −

//     If d is 0, and a = x, then return true, otherwise false.
//     Otherwise, if d is not 0, then if x belongs to the sequence x = a + n * d,
// where n is a non-negative integer, only if (n - a)/c is a non-negative integer.

#include <iostream>
using namespace std;
bool isInAP(int a, int d, int x)
{
    if (d == 0 and x == a)
        return 1;
    else if (d == 0 and x != a)
        return 0;
    else if ((x - a) % d == 0 and (x - a) / d >= 0)
        return 1;
    else
        return 0;
}

int main()
{
    int a = 1, x = 7, d = 3;
    if (isInAP(a, d, x))
        cout << "The value " << x << " is present in the AP";
    else
        cout << "The value " << x << " is not present in the AP";
}