#include <iostream>
#include <stdio.h>

using namespace std;
int *rverse(int arr[] , int start , int end)
{
   while (start < end)
    {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
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
    p = rverse(arr, 0 , d-1);
    p = rverse(p,d,n-1);
    p = rverse(p,0,n-1);
    for (int i=0 ; i<n ; i++)
    {
        printf("%d " , p[i]);
    }
    printf("\n");
}



