#include<stdio.h>
int main()
{
		//initialising row_A,row_B and sum
    int row_A=3;
    int row_B=3;
    int sum=0;
    //creating vector A as int type array
    int A[row_A];
    //initialising the elements of A
    A[0]=2;A[1]=-7;A[2]=6;
    // displaying vector A
    printf("A:");
    printf("[");
    //printing output in for loop
    for(int i=0;i<row_A;i++){
        //check for last element 
        if (i==row_A-1){
            printf("%d] ",A[i]);
        }
        else{
            printf("%d ,",A[i]);
        }
    }
    printf("\n\n");    
    //creating vector B as int type array
    int B[row_B];
    //initialising the elements of B
    B[0]=3;B[1]=2;B[2]=-7;
    //displaying vector B
    printf("B:");
    printf("[");
    //printing output in for loop
    for(int i=0;i<row_B;i++){
        //check for last element 
        if (i==row_B-1){
            printf("%d] ",B[i]);
        }
        else{
            printf("%d ,",B[i]);
        }
    }
    printf("\n\n"); 
    
    //performing vector addition
    //declaring A_add_B as an int type array
    int A_add_B[row_A];
    //calculating the elements of A_add_B using for loop
    for(int i=0;i<row_A;i++){
    		A_add_B[i]=A[i]+B[i];
    }
    //displaying vector addition 
    printf("A+B:");
    printf("[");
    //printing output in for loop
    for(int i=0;i<row_A;i++){
        //check for last element 
        if (i==row_A-1){
            printf("%d] ",A_add_B[i]);
        }
        else{
            printf("%d ,",A_add_B[i]);
        }
    }    
    printf("\n\n");
    //declaring A_dot_B as an int type variable
    int A_dot_B;
    //calculating scalar dot product using for loop
    for (int index=0;index<row_A;index++){
      	sum=sum+A[index]*B[index];
    }
		//storing sum in A_dot_B      
		A_dot_B=sum;
    //displaying scalar dot product
    printf("A.B: %d", A_dot_B); 
    printf("\n\n");
    return 0;
}
/*
//Output 

A:[2 ,-7 ,6] 

B:[3 ,2 ,-7] 

A+B:[5 ,-5 ,-1] 

A.B: -50

*/
