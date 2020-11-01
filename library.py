#importing everything from math module 
from math import *
#importing everything from random module
from random import *
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


    
#bracketing function
def bracketing(a,b,f,choice):
    factor=1.5
    count=0
    #using while loop to check bracketing of root and limit number of iterations of the loop
    while f(a,choice)*f(b,choice)>0 and count<12:
        #condition to update a
        if abs(f(a,choice))<abs(f(b,choice)):
            a=a-factor*(b-a)
        #condition to update b
        elif abs(f(a,choice))>abs(f(b,choice)):
            b=b+factor*(b-a)
        count+=1
    return a,b
#Bisection function
def Bisection(a,b,epsilon,f,choice):
    count=0
    #calling bracketing function
    a,b=bracketing(a,b,f,choice)
    print('No. of iterations    ','Absolute Error\n')
    #using while loop for convergence of a and b and limit number of iterations of the loop
    while abs(b-a)>epsilon and count<200:
        print(count,'                   ',abs(b-a),'\n')
        c=(a+b)/2
        #condition to update a and b
        if f(a,choice)*f(c,choice)<0:
            b=c
        elif f(a,choice)*f(c,choice)>0:
            a=c
        #checking whether a or c is a root 
        else:
            if f(a,choice)==0:
                print('Root obtained:',a)
            if f(c,choice)==0:
                print('Root obtained:',c)
        
        count+=1
        
    return a
#Regula_Falsi function
def Regula_Falsi(a,b,epsilon,f,choice):
    count=0
    #initial guess
    c=a
    d=b
    #calling bracketing function
    a,b=bracketing(a,b,f,choice)
    
    print('No. of iterations    ','Absolute Error\n')
    #using while loop for convergence of d and c and limit the number of iterations of the loop
    while abs(d-c)>epsilon and count<200:
        print(count,'                   ',abs(d-c),'\n')
        d=c
        c=b-(((b-a)*f(b,choice))/(f(b,choice)-f(a,choice)))
        
        #condition to update a and b
        if f(a,choice)*f(c,choice)<0:
            b=c
        elif f(a,choice)*f(c,choice)>0:
            a=c
        #checking whether a or c is a root 
        else:
            if f(a,choice)==0:
                print('Root obtained:',a)
            if f(c,choice)==0:
                print('Root obtained:',c)
        count+=1
        
    return c
#d1_f(x) function
def d1_f(x,f,choice):
    h=0.01
    y=(f(x+h,choice)-f(x-h,choice))/(2*h)
    return y

#Newton_Raphson function
def Newton_Raphson(x_0,epsilon,f,choice):
    count=0
    #initial guess
    x=0
    print('No. of iterations    ','Absolute Error\n')
    #using while loop for convergence of x_0 and x and limit the number of iterations of the loop
    while abs(x_0-x)>epsilon and count<200:
         
        print(count,'                   ',abs(x_0-x),'\n') 
        x=x_0
        x_0=x_0-(f(x_0,choice)/d1_f(x_0,f,choice))
        
        #checking whether x_0 is a root
        if f(x_0,choice)==0:
              print('Root Obtained:',x_0)
        
        count+=1
    return x_0

#d1_poly_f(x) function
def d1_poly_f(x,coeff,n,poly_f):
    h=0.01
    y=(poly_f(x+h,coeff,n)-poly_f(x-h,coeff,n))/(2*h)
    return y
#d^2_poly_f(x) function
def d2_poly_f(x,coeff,n,poly_f):
    h=0.01
    y=(d1_poly_f(x+h,coeff,n,poly_f)-d1_poly_f(x-h,coeff,n,poly_f))/(2*h)
    return y
#Laguerre function
def Laguerre(alpha_0,epsilon,coeff,n,poly_f):
    count=0
    #initial guess
    alpha=0
    #using while loop for convergence of alpha_0 and alpha and limit the number of iterations of the loop
    while abs(alpha_0-alpha)>epsilon and count<200:
        alpha=alpha_0
        G=d1_poly_f(alpha_0,coeff,n,poly_f)/poly_f(alpha_0,coeff,n)
        H=G**2-(d2_poly_f(alpha_0,coeff,n,poly_f)/poly_f(alpha_0,coeff,n))
        #conditions to calculate a
        if abs(G+sqrt((n-1)*(n*H-G**2)))>abs(G-sqrt((n-1)*(n*H-G**2))):
            a=n/(G+sqrt((n-1)*(n*H-G**2)))
        elif abs(G-sqrt((n-1)*(n*H-G**2)))>abs(G+sqrt((n-1)*(n*H-G**2))):
            a=n/(G-sqrt((n-1)*(n*H-G**2)))
        #checking whether alpha_0 is a root
        else:
            if poly_f(alpha_0,coeff,n)==0:
                print('One of the roots obtained:',round(alpha_0,6))
        alpha_0=alpha_0-a
        count+=1
    return alpha_0

#Synthetic_Division function
def Synthetic_Division(alpha_0,coeff):
    
    #checking whether abs(coeff) (corresponding to variable with power=degree of polynomial)=1
    if abs(coeff[0])!=1:
        for data in coeff:
            data=data/coeff[0]
    #updating the coeff of polynomial in a loop
    for k in range(0,len(coeff)-1):
        coeff[k+1]=alpha_0*coeff[k]+coeff[k+1]
    
    return coeff
#Midpoint function
def Midpoint(a,b,f,N):
    h = (b-a)/N
    sum=0
    #calculating sum in a for loop
    for index in range(N):
        sum=sum + h*(f(a+index*h)+f(a+(index+1)*h))/2
    return sum

#Trapezoidal function
def Trapezoidal(a,b,f,N):
    h = (b-a)/N
    sum=0
    #calculating sum in a for loop
    for index in range(N+1):
        #condition for first and last elements
        if index==0 or index==N:
            sum=sum+h*f(a+index*h)/2
        else:
            sum=sum+h*f(a+index*h)
    return sum
#Simpson function
def Simpson(a,b,f,N):
    h = (b-a)/N
    sum = 0
    #calculating sum in a for loop
    for index in range(N+1):
        #condition for first and last elements
        if index == 0 or index == N:
            sum=sum+h*f(a+index*h)/3
        #condition for odd elements
        elif index%2 == 1:
            sum=sum+4 * h * f(a + index*h)/3
        else:
            sum=sum+2 * h * f(a + index * h) / 3
    return sum
#Monte_Carlo function
def Monte_Carlo(a,b,f,N):
    inside_counter=0
    #calculating the number of random points (float type) inside the area under the curve f(x) in a loop
    for i in range(N):
        x = uniform(a, b)
        #condition to determine range of y
        if f(a)>f(b):
            max_f=f(a)
            y =uniform(0, f(a))
        elif f(b)>f(a):
            max_f=f(b)
            y=uniform(0,f(b))
        area=(max_f-0)*(b-a)
        #condition to increase inside_counter by 1
        if y<=f(x):
            inside_counter+=1
    #calculating the numerical integration result 
    result=(inside_counter/N)*area
    return result
