#include <stdio.h>
#include<iostream>

using namespace std;

int rotationCount(int arr[], int n)
{
  int cnt = 0;
  int i;
  for(i=0 ;i<n ; i++)
  {
      if(arr[i] > arr[i+1])
        break;
  }
  if(i+1 == n)
    cnt = 0;
  else
    cnt = i+1;
  return cnt;
}

int main(void)
{
   int arr[] = {4,5,6,7,8,9,10,1,2,3};
   int n = sizeof(arr)/ sizeof(arr[0]);
   int x;
   int result =rotationCount(arr, n);
   printf("Result = %d \n"  , result);
   return 0;
}
