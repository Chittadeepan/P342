#include <stdio.h>

int main(void) {
    // creating FILE variables
    FILE *fptr;
    FILE *fpt;
    // integer variable
    int num;
  
    // opening the file in write mode
    fptr = fopen("Matrix_M", "w");
  
    if (fptr != NULL) {
        printf("File created successfully!\n");
    }
    else {
        printf("Failed to create the file.\n");
        // exit status for OS that an error occurred
        return -1;
    }
  
    // user input for integer numbers
    printf("Enter the elements of Matrix M present in 'Matrix_M.txt': ");
    for (int i=0;i<9;i++) {
        scanf("%d", &num);
        putw(num, fptr);
    }
  
    // closing connection
    fclose(fptr);
    
    // integer variable
    int n;
  
    // opening the file in write mode
    fpt = fopen("Matrix_N", "w");
  
    if (fpt != NULL) {
        printf("File created successfully!\n");
    }
    else {
        printf("Failed to create the file.\n");
        // exit status for OS that an error occurred
        return -1;
    }
  
    // user input for integer numbers
    printf("Enter the elements  of Matrix N present in 'Matrix_N.txt': ");
    for (int i=0;i<9;i++) {
        scanf("%d", &n);
        putw(n, fpt);
    }
  
    // close connection
    fclose(fpt);


    //declaring x as an int type array
    int x[100];
    //initialising count
    int count=0;
    // opening file for reading
    fptr = fopen("Matrix_M", "r");
  
    // displaying matrix M
    printf("\nM:\n");
    while ( (num = getw(fptr)) != EOF ) {
        x[count]=num;
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
    fpt = fopen("Matrix_N", "r");
  
    // displaying matrix N
    printf("\nN:\n");
    while ( (n = getw(fpt)) != EOF ) {
        y[counter]=n;
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

 

    //declaring  M as 2 dimensional float type array
    float M[3][3];
    M[0][0]= x[0];M[0][1]= x[1];M[0][2]=x[2];M[1][0]=x[3];M[1][1]=x[4];M[1][2]=x[5];M[2][0]=x[6];M[2][1]=x[7];M[2][2]=x[8];
    //declaring N as 2 dimensional float type array
    float N[3][3];
    N[0][0]=y[0];N[0][1]=y[1];N[0][2]=y[2];N[1][0]=y[3];N[1][1]=y[4];N[1][2]=y[5];N[2][0]=y[6];N[2][1]=y[7];N[2][2]=y[8];

    //declaring A as 2 dimensional float type array
    float A[3][1];
    A[0][0]=2;A[1][0]=-7;A[2][0]=6;
  
    //calculating M×N
    //declaring MxN as float type array
    float MxN[3][3];
    //calculating the elements of 1st row of M×N
    MxN[0][0]=(M[0][0]*N[0][0])+ (M[0][1]*N[1][0]) +  (M[0][2]*N[2][0]);
    MxN[0][1]=(M[0][0]*N[0][1])+ (M[0][1]*N[1][1]) +  (M[0][2]*N[2][1]);
    MxN[0][2]=(M[0][0]*N[0][2])+ (M[0][1]*N[1][2]) +  (M[0][2]*N[2][2]);
    //calculating the elements of 2nd row of M×N
    MxN[1][0]=(M[1][0]*N[0][0])+ (M[1][1]*N[1][0]) +  (M[1][2]*N[2][0]);
    MxN[1][1]=(M[1][0]*N[0][1])+ (M[1][1]*N[1][1]) +  (M[1][2]*N[2][1]);
    MxN[1][2]=(M[1][0]*N[0][2])+ (M[1][1]*N[1][2]) +  (M[1][2]*N[2][2]);   
    //calculating the elements of 3rd row of M×N
    MxN[2][0]=(M[2][0]*N[0][0])+ (M[2][1]*N[1][0]) +  (M[2][2]*N[2][0]);
    MxN[2][1]=(M[2][0]*N[0][1])+ (M[2][1]*N[1][1]) +  (M[2][2]*N[2][1]);
    MxN[2][2]=(M[2][0]*N[0][2])+ (M[2][1]*N[1][2]) +  (M[2][2]*N[2][2]);
    //displaying M×N
    printf("M×N:\n");
    for (int i=0;i<3;i++){
        for (int j=0;j<3;j++){
            if (j==2){
                  printf("%f\n",MxN[i][j]);
            }
            else{
                  printf("%f    ",MxN[i][j]);
            }
        }
    }
    printf("\n\n");  
    /*output: M×N:
12    -14   -104
-23   105    7
93    160    31 
      */                      
    //calculating M×A
    //declaring MxA as float type array
    float MxA[3][1];
    //calculating the elements of 1st row of M×A
    MxA[0][0]=(M[0][0]*A[0][0])+ (M[0][1]*A[1][0]) +  (M[0][2]*A[2][0]);
    //calculating the elements of 2nd row of M×A
    MxA[1][0]=(M[1][0]*A[0][0])+ (M[1][1]*A[1][0]) +  (M[1][2]*A[2][0]);   
    //calculating the elements of 3rd row of M×A
    MxA[2][0]=(M[2][0]*A[0][0])+ (M[2][1]*A[1][0]) +  (M[2][2]*A[2][0]);
    //displaying M×A
    printf("M×A:\n");
    for (int i=0;i<3;i++){
        for (int j=0;j<1;j++){
            if (j==0){
                  printf("%f\n",MxA[i][j]);
            }
            else{
                  printf("%f    ",MxA[i][j]);
            }
        }
    }
    printf("\n\n"); 
    /* output: M×A:
98
-55
92 
*/
    return 0;
}
    