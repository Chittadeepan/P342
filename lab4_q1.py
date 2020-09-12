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
                #calculating the diagonal elements and upper triangular elements and storing them in matrix a in a loop
                for k in range(0,i):
                    a[i][j]=a[i][j]-(a[i][k]*a[k][j])
           #condition for lower triangular elements  
            elif i>j: 
                #calculating the lower triangular numerator elements and storing them in matrix a in a loop
                for k in range(0,j):
                    a[i][j]=a[i][j]-(a[i][k]*a[k][j])
                    
                #performing the final division of each element of a by u[j][j]
                a[i][j]=a[i][j]/a[j][j]

    return a,b

#forward_backward function
def forward_backward_substitution(a,b):

    #forward substitution
    #using for loop for traversing the number of rows 
    for i in range (0,len(a)):    
        #calculating the elements of y and storing it in matrix b in a loop
        for j in range(0,i): 
                b[i][0]=b[i][0]-(a[i][j]*b[j][0])
            
            
    
    #backward substitution
    #using for loop for traversing the number of rows
    for i in range(len(a)-1,-1,-1):
            #calculating the numerator elements of x and storing it in matrix b in a loop
            for j in range(len(a)-1,i,-1): 
                b[i][0]=b[i][0]-(a[i][j]*b[j][0])
            #performing the final division of each element of b by u[i][i]
            b[i][0]=b[i][0]/a[i][i]
    
    return b 
#main function
def main():
    #writing matrices in txt files and reading them from the files created by calling matrix_read_and_write function
    A=matrix_read_and_write("Matrix_A_lab4_q1.txt","1  0  1  2\n0  1  -2  0\n1  2  -1  0\n2  1  3  -2\n")
    B=matrix_read_and_write("Matrix_B_lab4_q1.txt","6\n-3\n-2\n0") 
    #displaying matrix A by calling display_matrix function
    print('Matrix A:')
    display_matrix(A)
    #displaying matrix B by calling display_matrix function
    print('Matrix B:')
    display_matrix(B) 
    
    #call LU_Decomposition function
    A,B=LU_Decomposition(A,B)
    #call forward_backward function
    B=forward_backward_substitution(A,B)
    #displaying Soln(X) by calling display_matrix function
    print('Soln(X):')
    display_matrix(B)

main()
'''
#Output:
Matrix A:
1                         0                         1                         2
0                         1                         -2                         0
1                         2                         -1                         0
2                         1                         3                         -2


Matrix B:
6
-3
-2
0


Soln(X):
1.0
-1.0
1.0
2.0
'''
