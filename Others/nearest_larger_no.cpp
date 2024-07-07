
// Compute nearest larger number by interchanging digits updated.
// Given 2 numbers a and b find the smallest number greater than b by interchanging the
// digits of a and if not possible print -1.

// Input Format:
// 2 numbers a and b separated by space.

// Output:
// A single number, greater than b
// If not possible print -1

// Example:
// Input:
// 459 500

// Output:
// 549

#include <bits/stdc++.h>
using namespace std;
int main()
{
    string a, b;
    cin >> a >> b;
    sort(a.begin(), a.end());
    string temp = a;
    int flag = 1;
    while (stoi(temp) <= stoi(b))
    {

        bool temp1 = next_permutation(a.begin(), a.end());
        temp = a;
        if (!temp1)
        {
            flag = 0;
            break;
        }
    }
    if (flag)
        cout << stoi(a) << endl;
    else
        cout << "-1";

    return 0;
}