#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int arr[10] = {1,2,3,4,5,6,7,8,9,10};
    int n = 10;
    int d;
    cout<<"Enter d : ";
    cin>>d;
    int temp[d];
    int i;
    for (i=0 ; i<d; i++)
    {
        temp[i] =arr[i];
    }
    for (int p=0 ; p<d ; p++)
    {
        printf("%d " , temp[p]);
    }
    printf("\n");
    printf(" i = %d \n" , i);
    int j;
    for (j=0 ; j<n-d ; j++,i++)
    {
        arr[j] = arr[i];

    }
    printf("i = %d , j = %d \n" , i , j);

    for (int k=0 ; k<d ; k++)
    {
        arr[j] = temp[k];
        j++;
    }

    for(i=0 ; i<n;i++)
    {
        cout<<arr[i]<< " ";
    }
}


