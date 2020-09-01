#partial_pivot function
def partial_pivot(a,b):
        n=len(a)
        
        #row r-loop 0, ..., n-2
        for r in range(0,n-1):
                #condition for partial pivot
                if  abs(a[r][r]) == 0:
                        #row r1-loop r+1, ..., n-1 
                        for r1 in range(r+1, n):
                                #comparing with other elements of same column
                                if abs( a[r1][r] ) > abs( a[r][r] ):
                                        #interchange augmented a[r1][] <-> a[r][]
                                        a[r1],a[r]=a[r],a[r1]
					#interchange b[r1] <-> b[r]
                                        b[r1],b[r]=b[r],b[r1]
                                        
                else:
                        #do nothing
                        pass
        
        return a,b

#Gauss_Jordan function
def Gauss_Jordan(a,b):
        
        n=len(a)
        #row r-loop 0, ..., n-1        
        for r in range(0,n):
		
                #call partial pivot function
                #a=partial_pivot(a)
                a,b=partial_pivot(a,b)
                #set pivot
                pivot = a[r][r]
                
                #column c-loop r, ..., n
                for c in range(r, n):
                        #change elements of matrix a along the row containing pivot
                        a[r][c] = a[r][c]/pivot
                #change elements of matrix b corresponding to the row containing pivot using for loop
                for c in range (0,len(b[r])):        
                        b[r][c] = b[r][c]/pivot
                #row r1-loop 0, ..., n-1
                for r1 in range(0,n):
                        #checking if element==pivot or element==0
                        if r1==r or a[r1][r]==0:
                                #do nothing
                                pass
                        else:
                                #set factor
                                factor = a[r1][r]
                                #column c-loop r, ..., n-1
                                for c in range(r,n):
                                        #change elements of matrix a along the rows which do not contain pivot
                                        a[r1][c] = a[r1][c] - factor*a[r][c]
                                #change elements of matrix b corresponding to the rows which do not contain pivot using for loop
                                for c in range (0,len(b[r1])):
                                        b[r1][c] = b[r1][c] - factor*b[r][c]
        return b

#matrix_multiplication function
def matrix_multiplication(a,b):
	#declaring axb as empty list
        axb=[]

        #using for loop for traversing the number of rows in a×b
        for k in range (0,len(a)):
                #initialising  m as an empty list
                m=[]
                #initialising l as the number of elements in a[k]
                l=len(a[k])
                #using another for loop for traversing the number of elements in each row of a×b
                for i in range(0,len(b[l-1])):
                        #initialising x
                        x=0
                        #using another for loop to calculate each element in each row of a×b
                        for j in range(0,l):
                                x=x+a[k][j]*b[j][i]
                        #appending each element in list m 
                        m.append(x)
     
                #appending list a within another list a×b
                axb.append(m)
        return axb               

#main function
def main():
        #read matrices from files
        #reading matrix A from Matrix_A_lab3_q3.txt
        with open("Matrix_A_lab3_q3.txt") as fptr:
                data=fptr.read()
        print('A:')
        print(data)
        a=data.split()
        print('\n')
        #reading matrix B from Matrix_B_lab3_q3.txt
        with open("Matrix_B_lab3_q3.txt")  as  fpt:
                data=fpt.read()
        print('B:')
        print(data)
        b=data.split()
        print('\n')
        #calling eval function for elements of a and storing them in a using for loop
        for index in range(len(a)):
                a[index]=eval(a[index])
        #calling eval function for elements of b and storing them in b using for loop
        for index in range(len(b)):
                b[index]=eval(b[index])
        #initialising A as 2 dimensional list 
        #storing the elements of a in A  
        A=[ [a[0],a[1],a[2]], [a[3],a[4],a[5]], [a[6],a[7],a[8]] ]
        #initialising B as 2 dimensional list 
        #storing the elements of b in B
        B=[ [b[0],b[1],b[2]], [b[3],b[4],b[5]], [b[6],b[7],b[8]] ]
        #call Gauss_Jordan function
        #storing the value returned by Gauss_Jordan function in B
        B=Gauss_Jordan(A,B)
        #displaying Soln(A^(-1)) by using two for loops
        print('Soln(A^(-1)):')
        for i in range(len(B)):
                for j in range(len(B[i])):
                        #checking for last element
                        if j==(len(B[i])-1):
                                print(B[i][j])
                        else:
                                print(B[i][j],end='        ')
        print('\n')
        
        #check A(A^(-1))=I
        #storing the elements of a in A to check A(A^(-1))=I
        A=[ [a[0],a[1],a[2]], [a[3],a[4],a[5]], [a[6],a[7],a[8]] ]
        #call matrix_multiplication function
        AxB=matrix_multiplication(A,B)
        #displaying A(A^(-1)) by using two for loops
        print('A(A^(-1)):')
        for i in range(len(AxB)):
                for j in range(len(AxB[i])):
                        #checking for last element
                        if j==(len(AxB[i])-1):
                                print(AxB[i][j])
                        else:
                                print(AxB[i][j],end='        ')
        print('\n\n')
main()	
'''
#Output
A:
 1  -3   7
-1   4  -7
-1   3  -6


B:
1  0  0
0  1  0
0  0  1


Soln(A^(-1)):
-3.0        3.0        -7.0
1.0        1.0        0.0
1.0        0.0        1.0


A(A^(-1)):
1.0        0.0        0.0
0.0        1.0        0.0
0.0        0.0        1.0




'''