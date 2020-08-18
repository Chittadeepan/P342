#include <stdio.h>

int main(void) {
  // creating a FILE variable
  FILE *fptr;
  FILE *fpt;
  // integer variable
  int num;
  
  // open the file in write mode
  fptr = fopen("Matrix_M", "w");
  
  if (fptr != NULL) {
    printf("File created successfully!\n");
  }
  else {
    printf("Failed to create the file.\n");
    // exit status for OS that an error occurred
    return -1;
  }
  
  // enter integer numbers
  printf("Enter some integer numbers [Enter -1 to exit]: ");
  while (1) {
    scanf("%d", &num);
    if (num != -1) {
      putw(num, fptr);
    }
    else {
      break;
    }
  }
  
  // close connection
  fclose(fptr);
  // integer variable
  int n;
  
  // open the file in write mode
  fpt = fopen("Matrix_N", "w");
  
  if (fpt != NULL) {
    printf("File created successfully!\n");
  }
  else {
    printf("Failed to create the file.\n");
    // exit status for OS that an error occurred
    return -1;
  }
  
  // enter integer numbers
  printf("Enter some integer numbers [Enter -1 to exit]: ");
  while (1) {
    scanf("%d", &n);
    if (n != -1) {
      putw(n, fpt);
    }
    else {
      break;
    }
  }
  
  // close connection
  fclose(fpt);


  
  int x[100];
  // open file for reading
  fptr = fopen("Matrix_M", "r");
  
  // display numbers
  printf("\nNumbers:\n");
  //while ( (num = getw(fptr)) != EOF ) {
  for (int i=0;i<100;i++){
    num=getw(fptr);
    printf("%d\n", num);
    x[i]=num;
  }
  
  printf("\nEnd of file.\n");
  
  // close connection
  fclose(fptr);

  int y[100];
  // open file for reading
  fpt = fopen("Matrix_N", "r");
  
  // display numbers
  printf("\nNumbers:\n");
  //while ( (num = getw(fptr)) != EOF ) {
  for (int i=0;i<100;i++){
    n=getw(fpt);
    printf("%d\n", n);
    y[i]=n;
  }
  
  printf("\nEnd of file.\n");
  
  // close connection
  fclose(fpt);

 

    //declaring  M as 2 dimensional float type array
    float M[3][3];
    M[0][0]= x[0];M[0][1]= x[1];M[0][2]=x[2];M[1][0]=x[3];M[1][1]=x[4];M[1][2]=x[5];M[2][0]=x[6];M[2][1]=x[7];M[2][2]=x[8];
    //declaring N as 2 dimensional float type array
    float N[3][3];
    N[0][0]=y[0];N[0][1]=y[1];N[0][2]=y[2];N[1][0]=y[3];N[1][1]=y[4];N[1][2]=y[5];N[2][0]=y[6];N[2][1]=y[7];N[2][2]=y[8];

    //declaring A as 2 dimensional float type array
    float A[3][3];
    A[0][0]=1;A[0][1]=0;A[0][2]=3;A[1][0]=2;A[1][1]=-1;A[1][2]=5;A[2][0]=-4;A[2][1]=3;A[2][2]=-2;
  
    //calculating M×N
    //declaring MxN as float type array
    float MxN[3][3];
    //calculating the elements of 1st row of M×N
    MxN[0][0]=(M[0][0]*N[0][0])+ (M[0][1]*N[1][0]) +  (M[0][2]*N[2][0]);
    MxN[0][1]=(M[0][0]*N[0][1])+ (M[0][1]*N[1][1]) +  (M[0][2]*N[2][1]);
    MxN[0][1]=(M[0][0]*N[0][2])+ (M[0][1]*N[1][2]) +  (M[0][2]*N[2][2]);
    //calculating the elements of 2nd row of M×N
    MxN[1][0]=(M[1][0]*N[0][0])+ (M[1][1]*N[1][0]) +  (M[1][2]*N[2][0]);
    MxN[1][1]=(M[1][0]*N[0][1])+ (M[1][1]*N[1][1]) +  (M[1][2]*N[2][1]);
    MxN[1][1]=(M[1][0]*N[0][2])+ (M[1][1]*N[1][2]) +  (M[1][2]*N[2][2]);   
    //calculating the elements of 3rd row of M×N
    MxN[2][0]=(M[2][0]*N[0][0])+ (M[2][1]*N[1][0]) +  (M[2][2]*N[2][0]);
    MxN[2][1]=(M[2][0]*N[0][1])+ (M[2][1]*N[1][1]) +  (M[2][2]*N[2][1]);
    MxN[2][2]=(M[2][0]*N[0][2])+ (M[2][1]*N[1][2]) +  (M[2][2]*N[2][2]);
    //displaying M×N
    printf("M×N:\n");
    for (int i=0;i<3;i++){
      for (int j=0;j<3;j++){
            if (j==5){
                  printf("%d\n",MxN[i][j]);
            }
            else{
                  printf("%d    ",MxN[i][j]);
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
    //declaring NxM as float type array
    float MxA[3][3];
    //calculating the elements of 1st row of N×M
    MxA[0][0]=(M[0][0]*A[0][0])+ (M[0][1]*A[1][0]) +  (M[0][2]*A[2][0]);
    MxA[0][1]=(M[0][0]*A[0][1])+ (M[0][1]*A[1][1]) +  (M[0][2]*A[2][1]);
    MxA[0][1]=(M[0][0]*A[0][2])+ (M[0][1]*A[1][2]) +  (M[0][2]*A[2][2]);
    //calculating the elements of 2nd row of N×M
    MxA[1][0]=(M[1][0]*A[0][0])+ (M[1][1]*A[1][0]) +  (M[1][2]*A[2][0]);
    MxA[1][1]=(M[1][0]*A[0][1])+ (M[1][1]*A[1][1]) +  (M[1][2]*A[2][1]);
    MxA[1][1]=(M[1][0]*A[0][2])+ (M[1][1]*A[1][2]) +  (M[1][2]*A[2][2]);   
    //calculating the elements of 3rd row of N×M
    MxA[2][0]=(M[2][0]*A[0][0])+ (M[2][1]*A[1][0]) +  (M[2][2]*A[2][0]);
    MxA[2][1]=(M[2][0]*A[0][1])+ (M[2][1]*A[1][1]) +  (M[2][2]*A[2][1]);
    MxA[2][2]=(M[2][0]*A[0][2])+ (M[2][1]*A[1][2]) +  (M[2][2]*A[2][2]);
    //displaying N×M
    printf("M×A:\n");
    for (int i=0;i<3;i++){
      for (int j=0;j<3;j++){
            if (j==2){
                  printf("%d\n",MxA[i][j]);
            }
            else{
                  printf("%d    ",MxA[i][j]);
            }
      }
    }
    printf("\n\n"); 
    /* output: M×A:
-40   30   -34
25    -13   48
-73   51   -49  
*/
    return 0;
}
    