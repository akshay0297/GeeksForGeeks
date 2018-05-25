#include <stdio.h>
#include<iostream>

using namespace std;

int rotatedSum(int arr[], int n, int x)
{
   int i;
   for(i=0 ; i<n ;i++)
        if(arr[i]>arr[i+1])
            break;
    int l = (i+1)%n;
    int r = i;
   while( l != r )
   {
        if(arr[l] + arr[r] == x)
            return 1;
        if(arr[l] + arr[r] < x)
            l = (l+1)%n;
        else
            r = (n+r-1)%n;

   }
   return -1;
}

int main(void)
{
   int arr[] = {4, 5,6,7,8,9,10 , 1 ,2 ,3};
   int n = sizeof(arr)/ sizeof(arr[0]);
   int x;
   cout<<"Enter Key :";
   cin >> x;
   int result = rotatedSum(arr, n, x);
   if(result == -1)
    printf("Pair doesn't exists ");
   else printf("Pair exists");
   return 0;
}
