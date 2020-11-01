from library import *
#f(x) function
def f(x):
    y=x/(1+x)
    return y
#main program
def main():
    #initialising lower bound (a) and upper bound(b)
    a=1
    b=3
    #solving the integral of f(x) by Midpoint method,Trapezoidal method and Simpson method
    print('Calculating the integral of given function by Midpoint method for various values of N:')
    
    #solving the numerical integration result by the Midpoint method for N=6,10 and 24
    print('N     Numerical Integration Result')
    print('6        ',Midpoint(a,b,f,6))#fixing N=6
    
    print('10       ',Midpoint(a,b,f,10))#fixing N=10

    print('24      ',Midpoint(a,b,f,24))#fixing N=24

    print('Calculating the integral of given function by Trapezoidal method for various values of N:')
    #solving the numerical integration result by the Trapezoidal method for N=6,10 and 24
    print('N     Numerical Integration Result')
    print('6       ',Trapezoidal(a,b,f,6))#fixing N=6
    
    print('10        ',Trapezoidal(a,b,f,10))#fixing N=10

    print('24        ',Trapezoidal(a,b,f,24))#fixing N=24
    print('Calculating the integral of given function by Simpson method for various values of N:')
    #solving the numerical integration result by the Simpson method for N=6,10 and 24
    print('N     Numerical Integration Result')
    print('6        ',Simpson(a,b,f,6))#fixing N=6 
    
    print('10        ',Simpson(a,b,f,10))#fixing N=10

    print('24        ',Simpson(a,b,f,24))#fixing N=24
    
    print('The analytical result of the integration of given function: 1.306852') 
main()
'''
#Output
Calculating the integral of given function by Midpoint method for various values of N:
N     Numerical Integration Result
6         1.3051226551226551
10        1.3062285968245722
24       1.3067443360227213
Calculating the integral of given function by Trapezoidal method for various values of N:
N     Numerical Integration Result
6        1.3051226551226551
10         1.3062285968245722
24         1.3067443360227213
Calculating the integral of given function by Simpson method for various values of N:
N     Numerical Integration Result
6         1.3068302068302067
10         1.3068497693110697
24         1.3068527256556821
The analytical result of the integration of given function: 1.306852
'''

    
