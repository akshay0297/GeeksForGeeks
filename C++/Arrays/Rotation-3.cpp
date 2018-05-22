#include <iostream>
#include <stdio.h>

using namespace std;
int *cyclicRotate(int arr[] , int n , int d)
{
    for(int i=0 ; i<d ; i++)
    {
        int x = arr[n-1];
        for(int j=n-1 ; j>0 ; j--)
        {
            arr[j] = arr[j-1];
        }
        arr[0] = x;
    }
    return arr;
}
int main()
{
    int arr[10] = {1,2,3,4,5,6,7,8,9,10};
    int n = 10;
    int d;
    cout<<"Enter d : ";
    cin>>d;
    int *p;
    p = cyclicRotate(arr , n , d);
    for (int i=0 ; i<n ; i++)
    {
        printf("%d " , p[i]);
    }
    printf("\n");
}



