
// https://www.interviewbit.com/problems/min-steps-in-infinite-grid/

// https://medium.com/solvingalgo/how-to-solve-algorithmic-problems-minimum-number-of-steps-in-an-infinite-grid-f6cd3df17e3


#include <iostream>
#include <vector>

using namespace std;

int coverPoints(vector<int> &x, vector<int> &y)
{
    // Get current x and y
    int curX = x[0];
    int curY = y[0];
    // Counter
    int count = 0;

    for (int i = 1; i < x.size(); i++)
    {
        // Get destination x and y
        int dstX = x[i];
        int dstY = y[i];

        // Compute count according to the number of moves required
        count += max(
            abs(dstX - curX),
            abs(dstY - curY));

        // Update the current position
        curX = dstX;
        curY = dstY;
    }

    return count;
}

int main()
{
    // Example usage
    vector<int> x = {1, 4, 7};
    vector<int> y = {2, 5, 8};

    int result = coverPoints(x, y);

    cout << "Minimum number of moves: " << result << endl;

    return 0;
}
