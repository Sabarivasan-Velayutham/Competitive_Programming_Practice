
// In the theory of numbers, square free numbers have a special place.

// A square free number is one that is not divisible by a perfect square (other than 1).
//  Thus 72 is divisible by 36 (a perfect square), and is not a square free number,
//   but 70 has factors 1, 2, 5, 7, 10, 14, 35 and 70.  As none of these are perfect
//    squares (other than 1), 70 is a square free number.

// For some algorithms, it is important to find out the square free numbers that divide a number.
// Note that 1 is not considered a square free number.

// In this problem, you are asked to write a program to find the number of square free
//  numbers that divide a given number.

// Input
// The only line of the input is a single integer N which is divisible by no prime number
// larger than 19

// Output
// One line containing an integer that gives the number of square free numbers (not including 1)

// Example:
// Input
// 20

// Output
// 3

// N=20
// If we list the numbers that divide 20, they are
// 1, 2, 4, 5, 10, 20

// 1 is not a square free number, 4 is a perfect square, and 20 is divisible by 4,
// a perfect square.  2 and 5, being prime, are square free, and 10 is divisible by 1,2,5 and 10,
//  none of which are perfect squares.  Hence the square free numbers that divide 20 are 2, 5, 10.
// Hence the result is 3.


#include <bits/stdc++.h>
using namespace std;

bool isSqaureFree(int n)
{
    // If n is even, make n = n/2, this will reduce the number of our loop iterations.
    if (n % 2 == 0)
        n = n / 2;

    // If 2 divides n again, it is not a square free number.
    if (n % 2 == 0)
        return false;

    // Now n must be odd.  So we can iterate only over the odd numbers.
    for (int k = 3; k <= sqrt(n); k = k + 2)
    {
        // if k is a factor.
        if (n % k == 0)
        {
            n = n / k;

            // If i divides n again, n is not a square free number.
            if (n % k == 0)
                return false;
        }
    }
    return true;
}

int countNumbers(int n)
{

    // final ans.
    int count = 0;
    // loop till square root of n to count the square-free divisors.
    for (int i = 2; i <= sqrt(n); i++)
    {
        // If i is a divisor of n.
        if (n % i == 0)
        {
            // if i is square-free.
            if (isSqaureFree(i))
                count++;

            if (isSqaureFree(n / i))
                count++;
        }
    }
    return count;
}

int main()
{

    int n;
    cin >> n;
    cout << countNumbers(n);
    return 0;
}