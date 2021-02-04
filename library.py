#importing everything from math module 
from math import *
#importing everything from random module
from random import *
#importing pyplot from matplotlib module
from matplotlib import pyplot
#importing Axes3D from mplot3d module
from mpl_toolkits.mplot3d import Axes3D
#matrix_read_and_write function
def matrix_read_and_write(file_a,data):
    #writing matrices in files
    with open(file_a,'w') as fptr:
        fptr.write(data)
    #reading matrices from files
    with open(file_a) as fptr:
        data=fptr.read()
        print(data)
    #A= [[eval(x) for x in line.split()] for line in data]        
    #return A
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
#Euler function
def Euler(x,y,n,h,f):
    print("     X                                  Y")
    #calculating for x less than range in a loop
    while x<=n:
        #displaying the solutions obtained
        print(x,"                              ",y)
        y = y + h*f(x,y)
        x = x + h
    return x,y
#Runge Kutta-4(RK4) function
def RK4(x,y,v,h,r,f_1,f_2):
    print("     X                                  Y")
    #calculating for x less than range in a loop
    if x<r:
        while x <= r:
            k1 = h*f_1(v)
            l1 = h*f_2(x,y,v)

            k2 = h * f_1(v+l1/2)
            l2 = h * f_2(x+h/2,y+k1/2, v+l1/2)

            k3 = h * f_1(v + l2 / 2)
            l3 = h * f_2(x + h / 2, y + k2 / 2, v + l2 / 2)

            k4 = h * f_1(v + l3 / 2)
            l4 = h * f_2(x + h / 2, y + k3 / 2, v + l3 / 2)
            #calculating y and v i.e z for further iterations
            y = y + 1/6*(k1+2*k2+2*k3+k4)
            v = v + 1/6*(l1+2*l2+2*l3+l4)
            x = x + h
            
            #displaying the solutions obtained
            print(x,"                              ",y)
            
    #calculating for x greater than range in a loop
    elif x>r:
        while x >= r:
            k1 = h*f_1(v)
            l1 = h*f_2(x,y,v)

            k2 = h * f_1(v+l1/2)
            l2 = h * f_2(x+h/2,y+k1/2, v+l1/2)

            k3 = h * f_1(v + l2 / 2)
            l3 = h * f_2(x + h / 2, y + k2 / 2, v + l2 / 2)

            k4 = h * f_1(v + l3 / 2)
            l4 = h * f_2(x + h / 2, y + k3 / 2, v + l3 / 2)
            #calculating y and v i.e z for further iterations
            y = y + 1/6*(k1+2*k2+2*k3+k4)
            v = v + 1/6*(l1+2*l2+2*l3+l4)
            x = x + h
            
            #displaying the solutions obtained
            print(x,"                              ",y)
    return x,y
#shooting method
def shooting_method(x_0,y_0,h,x_n,y_n,z_1,z_2,f_1,f_2):
    #calling RK4 function with initial values, estimated slopes and both the functions as parameters 
    print('\nFor z_1=',z_1,' as estimated slope, the values of x and y are obtained as:')
    x_1,y_1=RK4(x_0,y_0,z_1,h,x_n,f_1,f_2)
    print("\nFrom the first guess z_1=",z_1, "the corresponding value of y is obtained as",y_1," at t=",x_0)
    print('\nFor z_2=',z_2,' as estimated slope, the values of x and y are obtained as:')
    x_2,y_2=RK4(x_0,y_0,z_2,h,x_n,f_1,f_2)
    print("\nFrom the second guess z_2=",z_2, "the corresponding value of y is obtained as",y_2," at t=",x_n)
    #condition for y_1 and y_n to be close enough
    if abs(y_1-y_n)<0.000001:
        return y_1,z_1
    #condition for y_2 and y_n to be close enough
    elif abs(y_2-y_n)<0.000001:
        return y_2, z_2
    else:
    #calculating correct slope in a loop
        for i in range(50):
            #conditions to check y_1 and y_2 to be on opposite sides of y_n
            if y_1<y_n and y_2>y_n:
                u=z_1+(z_2-z_1)*(y_n-y_1)/(y_2-y_1)
            elif y_1>y_n and y_2<y_n:
                u=z_2+(z_1-z_2)*(y_n-y_2)/(y_1-y_2)
                y_1,y_2=y_2,y_1
            else:
                print("\nGuess another slope at  original position.")
                return y_2,z_2
            #calling RK4 function with the same initial values, correct slope and both the functions as parameters
            x_3,y_3=RK4(x_0,y_0,u,h,x_n,f_1,f_2)
            #condition for y_3 and y_n to be close enough
            if abs(y_3-y_n)<0.000001:
                return y_3,u
            else:
                print("\nFrom the calculated guess",u,"the corresponding value of y is obtained as",y_3,"at x=",x_n)
                if y_3<y_n:
                    y_1=u
                else:
                    y_2=u
        #condition for no solution
        print("\nThe given differential equation couldn't be solved after 50 iterations.")

#random_walk function
def random_walk(x,y,step_range,walk_range,file_a):
    
    #storing the initial position of walker for using it in each random walk in loop
    x_0=x
    y_0=y
    
    #initialising variables to calculate RMS distance, radial distance and average displacement along x-axis and y-axis in loop
    R_RMS=0
    R=0
    Sum=0
    Mean_x=0
    Mean_y=0
    #creating a file to store the position of walker along x-axis and y-axis during random walk
    with open(file_a,'w') as fptr:
        #calculating distance covered along x-axis and y-axis in two loops for given walk_range and given step_range
        for i in range(1,walk_range+1):
            #storing the initial position of walker so that walker can start from that position after completion of each random walk
            x=x_0
            y=y_0
            #creating empty list to store the position of walker along x-axis and y-axis during random walk
            X=[]
            Y=[]
            for j in range(1,step_range+1):
                theta= uniform(0,2 * pi)
                x=x+cos(theta)
                y=y+sin(theta)
                
                #conditions for choosing 5 random walks
                if i/20==1:
                    if j==1:
                        fptr.write("Set:1\n")
                        fptr.write("\nDistance along x-axis               Distance along y-axis\n\n")
                        
                    X.append(x)
                    Y.append(y)
                    fptr.writelines([str(x),'                      ',str(y),'\n'])
                    
                    if j==step_range:
                        #plotting Set:1
                        pyplot.plot(X,Y,color="blue",linestyle="--",marker=".")
                        fptr.write('\n\n')
                        print("After",step_range,"number of steps starting from (",x_0,",",y_0,") and",i,"random walks, the final position of random walker:(",x,",",y,") and the radial distance R=",R," .")
                     
                elif i/20==2:
                    if j==1:
                        fptr.write("Set:2\n")
                        fptr.write("\nDistance along x-axis               Distance along y-axis\n\n") 
                
                    X.append(x)
                    Y.append(y)
                    fptr.writelines([str(x),'                      ',str(y),'\n'])
                    
                    if j==step_range:
                        #plotting Set:2
                        pyplot.plot(X,Y,color="green",linestyle="--",marker=".")
                        fptr.write('\n\n')
                        print("After",step_range,"number of steps starting from (",x_0,",",y_0,") and",i,"random walks, the final position of random walker:(",x,",",y,") and the radial distance R=",R," .")
                     
                elif i/20==3:
                    if j==1:
                        fptr.write("Set:3\n")
                        fptr.write("\nDistance along x-axis               Distance along y-axis\n\n")

                    X.append(x)
                    Y.append(y) 
                    fptr.writelines([str(x),'                      ',str(y),'\n'])
                    
                    if j==step_range:
                        #plotting Set:3
                        pyplot.plot(X,Y,color="yellow",linestyle="--",marker=".")
                        fptr.write('\n\n')
                        print("After",step_range,"number of steps starting from (",x_0,",",y_0,") and",i,"random walks, the final position of random walker:(",x,",",y,") and the radial distance R=",R," .")
                    
                elif i/20==4:
                    if j==1:
                        fptr.write("Set:4\n")
                        fptr.write("\nDistance along x-axis               Distance along y-axis\n\n")
                
                    X.append(x)
                    Y.append(y)
                    
                    fptr.writelines([str(x),'                      ',str(y),'\n'])
                    
                    if j==step_range:
                        #plotting Set:4
                        pyplot.plot(X,Y,color="orange",linestyle="--",marker=".")
                        fptr.write('\n\n')
                        print("After",step_range,"number of steps starting from (",x_0,",",y_0,") and",i,"random walks, the final position of random walker:(",x,",",y,") and the radial distance R=",R," .") 
                    
                elif i/20==5:
                    if j==1:
                        fptr.write("Set:5\n")
                        fptr.write("\nDistance along x-axis               Distance along y-axis\n\n")
                
                    X.append(x)
                    Y.append(y)
                    fptr.writelines([str(x),'                      ',str(y),'\n'])
                    
                    if j==step_range:
                        #plotting Set:5
                        pyplot.plot(X,Y,color="red",linestyle="--",marker=".",)
                        fptr.write('\n\n')
                        print("After",step_range,"number of steps starting from (",x_0,",",y_0,") and",i,"random walks, the final position of random walker:(",x,",",y,") and the radial distance R=",R," .")
                    
            R=sqrt(pow(x,2)+pow(y,2))
            Sum=Sum+pow(R,2)
    Mean_x=x/walk_range
    Mean_y=y/walk_range
    R_RMS=sqrt(Sum/walk_range)
    print("\nAfter ", walk_range," number of random walks, RMS distance=",R_RMS,", average displacement along x-axis=",Mean_x,", average displacement along y-axis=",Mean_y,".")
              
        
    #displaying the plots of various random walks with given number of steps
    if j==250:  
                pyplot.title("Random Walk Plot for 250 steps")
                pyplot.xlabel("Distance along X axis")
                pyplot.ylabel("Distance along Y axis")
                pyplot.legend(["Random_Walk_1","Random_Walk_2","Random_Walk_3","Random_Walk_4","Random_Walk_5"])
                pyplot.show()
                
    elif j==500:
                pyplot.title("Random Walk Plot for 500 steps")
                pyplot.xlabel("Distance along X axis")
                pyplot.ylabel("Distance along Y axis")
                pyplot.legend(["Random_Walk_1","Random_Walk_2","Random_Walk_3","Random_Walk_4","Random_Walk_5"])
                pyplot.show()
            
    elif j==750:
                pyplot.title("Random Walk Plot for 750 steps")
                pyplot.xlabel("Distance along X axis")
                pyplot.ylabel("Distance along Y axis")
                pyplot.legend(["Random_Walk_1","Random_Walk_2","Random_Walk_3","Random_Walk_4","Random_Walk_5"])
                pyplot.show()
               
    elif j==1000: 
                pyplot.title("Random Walk Plot for 1000 steps")
                pyplot.xlabel("Distance along X axis")
                pyplot.ylabel("Distance along Y axis")
                pyplot.legend(["Random_Walk_1","Random_Walk_2","Random_Walk_3","Random_Walk_4","Random_Walk_5"])
                pyplot.show()
                
    elif j==1250: 
                pyplot.title("Random Walk Plot for 1250 steps")
                pyplot.xlabel("Distance along X axis")
                pyplot.ylabel("Distance along Y axis")
                pyplot.legend(["Random_Walk_1","Random_Walk_2","Random_Walk_3","Random_Walk_4","Random_Walk_5"])
                pyplot.show()
         
         
    print('\n\n')
    
#Monte_Carlo Simulation for volume
def monte_carlo_volume(g,h,i,p,q,r,f,N):
    #initialising variables to count the number of points that satisfy the f(x) equation
    inside_counter=0
    #creating empty list to store the coordinates along x-axis, y-axis and z-axis of points inside the f(x) equation
    X=[]
    Y=[]
    Z=[]
    if (N==12100):
        with open("Data for 3D Plot of volume of ellipsoid for 12100 points.txt",'a') as fptr:
            fptr.writelines(["N: ",str(N)])
            fptr.write("\n X Co-ordinate                              Y Co-ordinate                            Z Co-ordinate\n\n") 
    #calculating the number of random points (float type) inside the space under the curve f(x) in a loop
    for j in range(N):
            x = uniform(g,p)
            y= uniform(h,q)
            z= uniform(i,r)

            #condition for counting random points
            if f(x,y,z)<=1:
                inside_counter+=1
                if (N==12100):
                    with open("Data for 3D Plot of volume of ellipsoid for 12100 points.txt",'a') as fptr: 
                        fptr.writelines([str(x),'                      ',str(y),'                      ',str(z),'\n']) 
                    X.append(x)
                    Y.append(y)
                    Z.append(z)
                    
                
                
            
    #condition for plotting a 3D plot of f(x) equation  
    if (N==12100):
                #plotting a scatter plot of data points inside the f(x) equation
                fig=pyplot.figure()
                ax=fig.gca(projection='3d')
                ax.scatter(X,Y,Z,zdir='z')
                pyplot.title("3D Plot of Volume of Ellipsoid for 12,100 points")
                ax.set_xlabel("X-Coordinate")
                ax.set_ylabel("Y-Coordinate")
                ax.set_zlabel("Z-Coordinate")
                pyplot.legend(["Co-ordinate point inside the ellipsoid or on the surface of ellipsoid"])
                pyplot.show()
                
    #defining volume of entire space of points
    V=abs(p-g)*abs(q-h)*abs(r-i)
    
    #calculating the numerical integration result of f(x) equation
    result=(inside_counter/N)*V
    return result

#least_square_fitting function
def least_square_fitting(N,A):
    #initialising variables to calculate average of x,y,x^2,xy and residuals
    sum_x=0
    sum_y=0
    sum_x2=0
    sum_y2=0
    sum_xy=0
    sum_error=0#R^2
    #determination of slope and intercept
    print("Total number of observations:",N)
    for i in range (N):
        x=A[i][0]
        print('Time:',x)
        y=A[i][1]
        print('Angular velocity:',y)
        '''
        #xy=x*y
        #print(xy)
        
        #print(x2)
        '''
        sum_x=sum_x+x
        sum_x2=sum_x2+x**2
        sum_xy=sum_xy+x*y
        sum_y=sum_y+y
        sum_y2=sum_y2+y**2
        
        print('\n')
    mean_x=sum_x/N
    
    mean_y=sum_y/N
    mean_xy=sum_xy/N
    mean_x2=sum_x2/N

    S_xx=sum_x2-N * mean_x ** 2
    print("S_xx:",S_xx)
    delta=N*S_xx
    S_yy=sum_y2-N * mean_y ** 2
    print("S_yy:",S_yy)
    S_xy=sum_xy-N * mean_x * mean_y
    print("S_xy:",S_xy)
    sig_x =sqrt(abs(S_xx/N)) #standard deviation of x
    sig_y =sqrt(abs(S_yy/N)) #standard deviation of y
    sig_xy =sqrt(abs(S_xy/N)) #square root of co-variance of x,y

    intercept_1=(mean_y*sum_x2-mean_x*sum_xy)/S_xx
    slope=S_xy/S_xx
    print('\nSlope:',slope)
    intercept_2=mean_y-slope*mean_x
    print('Intercept:',intercept_2,'\n')
    #slope and intercept are regression coeff
    
    r=sqrt(S_xy**2/(S_xx*S_yy))#pearson's r correlation coeff quality of fit
    print("Pearson's r:",r)
    #R^2 calculation
    for j in range(N):
        x=A[j][0]
        y=A[j][1]
        error=y-slope*x-intercept_1
        #print('square of error:',error**2) 
        sum_error=sum_error + error**2
    #print('R^2:',sum_error)

    #standard error calculation
    #standard=stanadard deviation/sqrt(N)
    S=sqrt((S_yy-slope*S_xy)/(N-2))
    SE_intercept=S*sqrt(1/N + mean_x**2/S_xx)#standard error in intercept
    SE_slope=S/sqrt(S_xx)#standard error in slope

    #print('Error in slope:',SE_slope)
    #print('Error in intercept:',SE_intercept)
    return slope,intercept_2,r
#practice functions
def standard_deviation_1(N,A):
    sum_x=0
    Sum=0
    for i in range(N):
        x=A[i]
        sum_x=sum_x+x

    mean_x=sum_x/N
    for j in range(N):
        x=A[j]
        Sum=Sum + (x-mean_x)**2        
    #calculating various sigma
    sig_n_1=sqrt(Sum/N)#biased estimator of variance if actual mean given
    sig_n_2=sqrt(Sum/(N-1))#unbiased estimator of variance to estimate mean
    sig_n_3=sqrt((Sum-Sum/N)/(N-1))#2 pass algorithm strict standard deviation
    return sig_n_1,mean_x

def standard_deviation_2(N,A):
    sum_data=0
    sum_n=0
    Sum=0
    #calculating Sum of all values and total number of observations in loop
    for i in range(N):
        n=A[i][0]
        mean=A[i][1]
        sum_data=sum_data+n*mean
        sum_n=sum_n+n
        
    mean_data=sum_data/sum_n
    
    for j in range (N):
        sigma=A[i][2]
        mean=A[i][1]
        d=mean-mean_data
        Sum=Sum+n*(sigma**2+d**2)
    #calculating net standard deviation    
    sigma_data=sqrt(Sum/sum_n)
    return mean_data,sigma_data

def standard_deviation_3(number,A):
    Sum=0
    Sum_N=0
    Product_N=1
    mean_x=A[0][1]
    mean_y=A[1][1]
    for i in range(number):
        N=C[i][0]
        mean_data=A[i][1]
        sigma_data=A[i][2]
        Sum=Sum+(N-1)**2*sigma_data**2
        Sum_N=Sum_N+N
        Product_N=Product_N*N
        
    #calculating overall standard deviation for both standard deviation along x and y directions
    Grand_Sum=Sum_N+ (Product_N/Sum_N)*(mean_x-mean_y)**2
    Grand_Sigma=Grand_Sum/(Sum_N-1)
    return Grand_Sigma
    #S_N=2/3(M_N)+1/3(T_N) S_n-Simpson M_N-midpoint T_N-trapezoidal
