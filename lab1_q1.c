#include<stdio.h>

int main()
{
    // declaring n as integer
    int n;
    //user input
    printf("Enter the natural number upto which you want to find the sum of all its previous numbers: ");
    scanf("%d",&n);
    printf("\n");
    // initialising sum and index
    int sum=0;
    int index=1;
    //checking boundary conditions 
    if(n<1){
        printf("The given input is not a natural number.");
    }
    else{
        // calculating sum in for loop
        while (index<=n){
            sum=sum+index;
            ++index;
        }
        // displaying output
        printf("Sum of first %d natural numbers: %d\n",n,sum);
    }
    printf("\n\n");
    return 0;
}