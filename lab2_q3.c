#include <stdio.h>

int main(void) {
    // creating FILE variables
    FILE *fptr;
    FILE *fpt;
    // initialising int type array
    int num[9]={4,-6,8,3,7,-2,-5,0,17};
  
    // opening the file in write mode
    fptr = fopen("Matrix_M_lab2", "w");
  
    if (fptr != NULL) {
        printf("File created successfully!\n");
    }
    else {
        printf("Failed to create the file.\n");
        // exit status for OS that an error occurred
        return -1;
    }
  
    // writing the elements of matrix M in file
    for (int i=0;i<9;i++) {
        putw(num[i], fptr);
    }
  
    // closing connection
    fclose(fptr);
    
    // initialising int type array
    int n[9]={-5,2,-13,0,17,6,4,10,-2};
  
    // opening the file in write mode
    fpt = fopen("Matrix_N_lab2", "w");
  
    if (fpt != NULL) {
        printf("File created successfully!\n");
    }
    else {
        printf("Failed to create the file.\n");
        // exit status for OS that an error occurred
        return -1;
    }
  
    // writing the elements of matrix N in file
  
    for (int i=0;i<9;i++) {
        putw(n[i], fpt);
    }
  
    // close connection
    fclose(fpt);


    //declaring x as an int type array
    int x[100];
    //initialising count
    int count=0;
    // opening file for reading
    fptr = fopen("Matrix_M_lab2", "r");
  
    // displaying matrix M
    printf("\nM:\n");
    while ( (num[count] = getw(fptr)) != EOF ) {
        x[count]=num[count];
        count++;
    }
    count=0;
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            if(j==2){
                printf("%d\n",x[count]);
            }
            else{
                printf("%d    ",x[count]);
            }
            count++;
        }
    }
  
  
    printf("\nEnd of file.\n");
  
    // closing connection
    fclose(fptr);


    //declaring y as an int type array
    int y[100];
    //initialising counter
    int counter=0;
    // opening file for reading
    fpt = fopen("Matrix_N_lab2", "r");
  
    // displaying matrix N
    printf("\nN:\n");
    while ( (n[counter] = getw(fpt)) != EOF ) {
        y[counter]=n[counter];
        counter++;
    }
    counter=0;
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            if(j==2){
                printf("%d\n",y[counter]);
            }
            else{
                printf("%d    ",y[counter]);
            }
            counter++;
        }
    }
  
    printf("\nEnd of file.\n");
  
    // closing connection
    fclose(fpt);

		//initialising row_M,col_M,row_N,col_N, row_A and col_A as int type variables
		int row_M=3;
		int col_M=3;
		int row_N=3;
		int col_N=3;
		int row_A=3;
		int col_A=1;
	  //declaring  M as 2 dimensional float type array
    float M[row_M][col_M];
    //initialising the elements of M
    M[0][0]= x[0];M[0][1]= x[1];M[0][2]=x[2];M[1][0]=x[3];M[1][1]=x[4];M[1][2]=x[5];M[2][0]=x[6];M[2][1]=x[7];M[2][2]=x[8];
    //declaring N as 2 dimensional float type array
    float N[row_N][col_N];
    //initialising the elements of N
    N[0][0]=y[0];N[0][1]=y[1];N[0][2]=y[2];N[1][0]=y[3];N[1][1]=y[4];N[1][2]=y[5];N[2][0]=y[6];N[2][1]=y[7];N[2][2]=y[8];

    //declaring A as 2 dimensional float type array
    float A[row_A][col_A];
    //initialising the elements of A
    A[0][0]=2;A[1][0]=-7;A[2][0]=6;
  
    //calculating M×N
    //declaring MxN as float type array
    float MxN[row_M][col_N];
		//using for loop for traversing the number of rows in M×N
		for (int k=0;k<row_M;k++){
				//using another for loop for traversing the number of elements in each row of M×N
      	for (int i=0;i<col_N;i++){
						//initialising x as float type variable 
            float x=0;
            //using another for loop to calculate each element in each row of M×N
            for (int j=0;j<col_M;j++){
            		x=x+M[k][j]*N[j][i];
            }
            //storing x in kth row and ith column of MxN
            MxN[k][i]=x;
				}
		}
    //displaying M×N
    printf("M×N:\n");
    for (int i=0;i<row_M;i++){
        for (int j=0;j<col_N;j++){
            if (j==col_N-1){
                  printf("%f\n",MxN[i][j]);
            }
            else{
                  printf("%f   ",MxN[i][j]);
            }
        }
    }
    printf("\n\n");  
                          
    //calculating M×A
    //declaring MxA as float type array
    float MxA[row_M][col_A];
    //using for loop for traversing the number of rows in M×A
		for (int k=0;k<row_M;k++){
      	//using another for loop for traversing the number of elements in each row of M×A
      	for (int i=0;i<col_A;i++){
						//initialising x as float type variable 
            float x=0;
            //using another for loop to calculate each element in each row of M×A
            for (int j=0;j<col_M;j++){
            		x=x+M[k][j]*A[j][i];
            }
            //storing x in kth row and ith column of MxA
            MxA[k][i]=x;
				}
		}
    //displaying M×A
    printf("M×A:\n");
    for (int i=0;i<row_M;i++){
        for (int j=0;j<col_A;j++){
            if (j==col_A-1){
                  printf("%f\n",MxA[i][j]);
            }
            else{
                  printf("%f    ",MxA[i][j]);
            }
        }
    }
    printf("\n\n"); 
    
    return 0;
}
/*
//Output

File created successfully!
File created successfully!

M:
4    -6    8
3    7    -2
-5    0    17

End of file.

N:
-5    2    -13
0    17    6
4    10    -2

End of file.
MN:
12.000000   -14.000000   -104.000000
-23.000000   105.000000   7.000000
93.000000   160.000000   31.000000


MA:
98.000000
-55.000000
92.000000



*/    
      
