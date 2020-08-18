#include<stdio.h>

int main()
{
    //creating vector A
    int A[3]={2,-7,6};
    // displaying vector A
    printf("A:");
    printf("[");
    int i,index=0;
    //printing output in for loop
    for(i=0;i<3;i++){
        //check for last element 
        if (i==2){
            printf("%d] ",A[i]);
        }
        else{
            printf("%d ,",A[i]);
        }
    }
    printf("\n\n");    
    //creating vector B
    int B[3]={3,2,-7};
    //displaying vector B
    printf("B:");
    printf("[");
    //printing output in for loop
    for(i=0;i<3;i++){
        //checking for last element 
        if (i==2){
            printf("%d] ",B[i]);
        }
        else{
            printf("%d ,",B[i]);
        }
    }
    printf("\n\n");  
    //performing vector addition
    int A_add_B[3]={A[0]+B[0],A[1]+B[1],A[2]+B[2]};
    //displaying vector addition 
    printf("A+B:");// Output:[5 ,-5 ,-1]
    printf("[");
    //printing output in for loop
    for(i=0;i<3;i++){
        //checking for last element 
        if (i==2){
            printf("%d] ",A_add_B[i]);
        }
        else{
            printf("%d ,",A_add_B[i]);
        }
    }    
    printf("\n\n");
    //calculating scalar dot product
    int A_dot_B=(A[0]*B[0])+(A[1]*B[1])+(A[2]*B[2]);
    //displaying scalar dot product
    printf("A.B: %d", A_dot_B);//Output:-50 
    printf("\n\n");
    return 0;
}