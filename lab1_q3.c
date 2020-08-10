#include<stdio.h>

int main()
{
    //initialising sum and index
    float sum=0.0;
    float index=1;
    //using while loop to find sum
    while (1/index>=0.001){
        sum=sum + 1/index;
        index++;
    }
    //displaying output
    printf("Summing over 1 + 1/2 + 1/3...  till sum does not change by more than 0.001: %lf",sum);
    printf("\n\n");
    return 0;
}