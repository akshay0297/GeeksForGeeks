#include <stdio.h>
#include<iostream>

using namespace std;

int maxSum(int arr[], int n)
{
    int as=0 , cv = 0;
    for(int i=0 ;i<n ;i++)
    {
        as = as + arr[i];
        cv = cv + i*arr[i];
    }

    int mv = cv;

    for(int j=1 ; j<n ; j++)
    {
        cv = cv + as - n*arr[n-j];
        if(cv > mv)
            mv = cv;
    }

    return mv;
}

int main(void)
{
   int arr[] = {4, 5,6,7,8,9,10 , 1 ,2 ,3};
   int n = sizeof(arr)/ sizeof(arr[0]);
   int x;
   int result = maxSum(arr, n);
   printf("Result = %d \n"  , result);
   return 0;
}
