from math import *
from library import *
#f(x) function
def f(x):
    y = exp(-x**2)
    return y
#main program
def main():
    #initialising maximum error,lower bound (a) and upper bound(b)
    max_error = 0.001
    a=0
    b=1
    #2nd derivative of f is obtained by hand calculation as 0.99501
    d2_f=0.99501
    #4th derivative of f is obtained by hand calculation as 12
    d4_f=12
    print('Maximum error allowed:',max_error)
    
    #calculating N for Midpoint method
   N_Midpoint = ceil(sqrt((b-a)**3*d2_f/(24*max_error)))
    
    #calculating N for Trapezoidal method 
    N_Trapezoidal = ceil(sqrt((b-a)**3*d2_f/(12*max_error)))

    #calculating N for Simpson method
    N_Simpson = ceil(pow((b-a)**5*d4_f/(180*max_error),1/4))

    #solving the integral of f(x) by Midpoint method,Trapezoidal method and Simpson method
    print("Numerical Integration Result obtained by Midpoint method:",Midpoint(0,1,f,N_Midpoint))
    print("Numerical Integration Result obtained by Trapezoidal method:",Trapezoidal(0,1,f,N_Trapezoidal))
    print("Numerical Integration Result obtained by Simpson method:",Simpson(0,1,f,N_Simpson+1))#increasing N_Simpson by 1 to provide even N for Simpson's Method
main()
'''
#Output
Maximum error allowed: 0.001
Numerical Integration Result obtained by Midpoint method: 0.7455719918300938
Numerical Integration Result obtained by Trapezoidal method: 0.7462107961317492
Numerical Integration Result obtained by Simpson method: 0.7468553797909872
'''
