#matrix_read_and_write function
def matrix_read_and_write(file_a,data):
    #writing matrices in files
    with open(file_a,'w') as fptr:
        fptr.write(data)
    #reading matrices from files
    with open(file_a) as fptr:
        data=fptr.readlines()
    A= [[eval(x) for x in line.split()] for line in data]        
    return A
#display_matrix function
def display_matrix(a):
    for i in range(len(a)):
            for j in range(len(a[i])):
                    #checking for last element
                    if j==(len(a[i])-1):
                        print(a[i][j])
                    else:
                        print(a[i][j],end='                         ')
    print('\n')
    
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
                                if abs( a[r1][r] ) > abs( a[r][r] ) and abs(a[r][r]) == 0:
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
     
                #appending list m within another list a×b
                axb.append(m)
        return axb
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
                #performing the final division of each element of b by u[i][i]
                b[i][j]=b[i][j]/a[i][i]
    
    return b
