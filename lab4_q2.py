#importing all the functions from library_lab4
from library_lab4 import *
#LU_Decomposition function
def LU_Decomposition(a,b):
    
    #using for loop for traversing the number of columns
    for j in range (0,len(a[len(a)-1])):
        #call partial pivot function
        a,b=partial_pivot(a,b) 
        
        #using another for loop for traversing the number of rows
        for i in range (0,len(a)):
            
            #condition for diagonal elements and upper triangular elements
            if i==j or i<j:
                #using another for loop to calculate diagonal elements and upper triangular elements
                for k in range(0,i):
                    #storing the elements obtained in a
                    a[i][j]=a[i][j]-(a[i][k]*a[k][j])
                
            #condition for lower triangular elements  
            elif i>j:
                
                #using another for loop to calculate the lower triangular elements
                for k in range(0,j):
                    #storing the elements obtained in a
                    a[i][j]=a[i][j]-(a[i][k]*a[k][j])
                #performing the final division of each element by u[j][j]
                a[i][j]=a[i][j]/a[j][j]
            
    return a,b
#forward_backward function
def forward_backward_substitution(a,b):
    
    #forward substitution
    #using for loop for traversing the number of rows
    for i in range (0,len(a)):
        
        #using for loop for traversing the number of columns
        for j in range (0,len(a[i])):            
            
            #calculating the elements of y and storing it in matrix b in a loop
            for k in range(0,i): 
                    b[i][j]=b[i][j]-(a[i][k]*b[k][j])
            
    #backward substitution
    #using for loop for traversing the number of rows
    for i in range(len(a)-1,-1,-1):
        #using for loop for traversing the number of columns
        for j in range(len(a)-1,-1,-1):
                #calculating the numerator elements of x and storing it in matrix b in a loop
                for k in range(len(a)-1,i,-1): 
                    b[i][j]=b[i][j]-(a[i][k]*b[k][j])
                #performing the final division of each element by u[j][j]
                b[i][j]=b[i][j]/a[i][i]
    
    return b 

#main function
def main():
    #writing matrices in txt files and reading them from the files created by calling matrix_read_and_write function
    A=matrix_read_and_write("Matrix_A_lab4_q2.txt","0  2  8  6\n0  0  1  2\n0  1  0  1\n3  7  1  0\n")
    B=matrix_read_and_write("Matrix_B_lab4_q2.txt","1  0  0  0\n0  1  0  0\n0  0  1  0\n0  0  0  1") 
    #displaying matrix A by calling display_matrix function
    print('Matrix A:')
    display_matrix(A)
    #displaying matrix B by calling display_matrix function
    print('Matrix B:')
    display_matrix(B) 
    
    #call LU_Decomposition function
    #storing the values returned by LU_Decomposition function in A,B
    A,B=LU_Decomposition(A,B)
    #checking whether inverse of the given matrix exists
    det=1
    #calculating det in aloop
    for i in range(0,len(A)):
        det=det*A[i][i]
        
    print("Determinant of the given matrix after LU Decomposition:",det,"\n")

    print('As the determinant of the given matrix is not equal to 0, the inverse of the given matrix exists.\n') 
    
    #call forward_backward function
    B=forward_backward_substitution(A,B)
    #displaying Soln(X) by calling display_matrix function
    print('Soln(A^(-1)):')
    display_matrix(B)
    
main()
'''
#Output:
Matrix A:
0                         2                         8                         6
0                         0                         1                         2
0                         1                         0                         1
3                         7                         1                         0


Matrix B:
1                         0                         0                         0
0                         1                         0                         0
0                         0                         1                         0
0                         0                         0                         1


Determinant of the given matrix after LU Decomposition: -36.0

As the determinant of the given matrix is not equal to 0, the inverse of the given matrix exists.

Soln(A^(-1)):
-0.24999999999999997                         1.6666666666666663                         -1.8333333333333337                         0.3333333333333333
0.08333333333333333                         -0.6666666666666666                         0.8333333333333334                         0.0
0.16666666666666666                         -0.33333333333333326                         -0.3333333333333333                         0.0
-0.08333333333333333                         0.6666666666666666                         0.16666666666666666                         -0.0
'''
