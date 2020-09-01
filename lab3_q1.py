#partial_pivot function
def partial_pivot(a,b):
        n=len(a)
        
        #row r-loop 0, ..., n-2
        for r in range(0,n-1):
                #condition for partial pivot
                if  abs(a[r][r]) == 0:
                        #row r1-loop r+1, ..., n-1 
                        for r1 in range(r+1,n):
                                #comparing with other elements of same column
                                if abs( a[r1][r] ) > abs( a[r][r] ):
                                        #interchange a[r1][] <-> a[r][]
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
                a,b=partial_pivot(a,b)
                #set pivot
                pivot = a[r][r]
                
                #column c-loop r, ..., n
                for c in range(r, n):
                        #change elements of  matrix a along the row containing pivot
                        a[r][c] = a[r][c]/pivot
                #change elements of  matrix b corresponding to the row containing pivot using for loop       
                b[r][0] = b[r][0]/pivot
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
                                        #change elements of  matrix a along the rows which do not contain pivot
                                        a[r1][c] = a[r1][c] - factor*a[r][c]
                                #change elements of matrix b corresponding to the rows which do not contain pivot using for loop
                                b[r1][0] = b[r1][0] - factor*b[r][0]
        return b

#main function
def main():
        #read matrices from files
        #reading matrix A from Matrix_A_lab3_q1.txt
        with open("Matrix_A_lab3_q1.txt") as fptr:
                data=fptr.read()
        print('A:')
        print(data)
        a=data.split()
        print('\n')
        #reading matrix B from Matrix_B_lab3_q1.txt
        with open("Matrix_B_lab3_q1.txt")  as  fpt:
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
        B=[ [b[0]], [b[1]], [b[2]] ]
        #call Gauss_Jordan function
        #storing the value returned by Gauss_Jordan function in B
        B=Gauss_Jordan(A,B)
        #displaying Soln(X) by using two for loops
        print('Soln(X):')
        for i in range(len(B)):
                for j in range(len(B[i])):
                        #checking for last element
                        if j==(len(B[i])-1):
                                print(B[i][j])
                        else:
                                print(B[i][j],end='        ')
        print('\n\n')	

main()	
'''
#Output
A:
1  3  2
2  7  7
2  5  2


B:
 2
-1
 7


Soln(X):
3.0
1.0
-2.0





'''