#include<iostream>
using namespace std;
int main()
# Missing number in an array form 1 to 10
{
    int arr[10], sum=0;
    cout<<"Enter 9 numbers b/w 1 and 10\n";
    for (int i=0; i<10; i++)
    {
        cin>>arr[i];
        sum+=i;
    }
    int total=10*11/2;
    cout<<"Missing number is "<<total-sum;
}
