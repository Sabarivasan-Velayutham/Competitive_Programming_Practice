
// input 
// 2
// 10
// 100

// output
// 23
// 2318

#include <iostream>
using namespace std;

long long calculateSum(long n, long m)
{
    long long p = (n - 1) / m;
    return m * p * (p + 1) / 2;
}

int main()
{
    int t;
    long long sum = 0;
    cin >> t;
    for (int a0 = 0; a0 < t; a0++)
    {
        long long n;
        cin >> n;
        sum = calculateSum(n, 3) + calculateSum(n, 5) - calculateSum(n, 15);
        cout << sum << endl;
    }
    return 0;
}