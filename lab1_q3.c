#include<stdio.h>

int main()
{
    //initialising number, sum and index
    float number=0.001;
    float sum=0.0;
    float index=1;
    //assigning 1/number to a float type variable n to get the input for the last index of while loop
    float n=1/number;
    //using while loop to find sum
    while (index<n){
        sum=sum + 1/index;
        index++;
    }
    //displaying output
    printf("Summing over 1 + 1/2 + 1/3...  till sum does not change by more than 0.001: %lf",sum);
    printf("\n\n");
    return 0;
}