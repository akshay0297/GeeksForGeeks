#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int myCompare(string X, string Y)
{
    string XY = X.append(Y);
    string YX = Y.append(X);
    return XY.compare(YX) > 0 ? 1: 0;
}

void printLargest(vector<string> arr)
{
    sort(arr.begin(), arr.end(), myCompare);
    for (int i=0; i < arr.size() ; i++ )
        cout << arr[i];
}


int main()
{
    vector<string> arr;

    arr.push_back("1");
    arr.push_back("34");
    arr.push_back("3");
    arr.push_back("98");
    arr.push_back("9");
    arr.push_back("76");
    arr.push_back("45");
    arr.push_back("4");
    printLargest(arr);


    return 0;
}
