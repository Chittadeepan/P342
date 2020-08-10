#include<stdio.h>

int main()
{
    //declaring n as an integer
    int n;    
    //user input
    printf("Enter an integer whose factorial you want:");
    scanf("%d",&n);
    printf("\n");
    //initialising fact and index 
    int fact=1;
    int index=1;
    //checking for positive integers
    if (n>0){
        //calculating factorial in while loop
        while (index<=n){
            fact=fact*index;
            ++index;
        }
        // displaying output
        printf("The factorial of %d : %d",n,fact);
    }
    //checking boundary conditions 
    //base case
    else if(n==0){
        printf("The factorial of %d: %d",n,fact);
    }
    // checking  boundary conditions 
    else{
        printf("The given input is not a non-negative integer!");
    }
    printf("\n\n");
    return 0;
}