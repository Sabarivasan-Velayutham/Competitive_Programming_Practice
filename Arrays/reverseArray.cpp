
#include <vector>
#include <iostream>
using namespace std;

int main()
{
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 8};
    int len = arr.size();
    for (int i = 0; i < len; i++)
        cout << arr[i] << " ";
    cout << "\nAfter reversing array...\n";

    int temp;
    int j = len - 1;
    for (int i = 0; i < len / 2; i++)
    {
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        j--;
    }

    for (int i = 0; i < len; i++)
        cout << arr[i] << " ";
}