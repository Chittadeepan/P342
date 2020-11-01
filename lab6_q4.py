from library import *
#f(x) function
def f(x):
    y = 4/(1+ x**2)
    return y
#main program
def main():
    #initialising lower bound (a) and upper bound(b)
    a=0
    b=1

    #solving the integral of f(x) by Monte Carlo method
    print('Calculating the integral of given function by Monte Carlo method for various values of N:')
    print('N     Numerical Integration Result')
    #solving the numerical integration result by Monte Carlo method in two loops
    for power in range(1,5):
        for multiple in range(1,10):
            print(10**power*multiple,'            ',Monte_Carlo(a,b,f,10**power*multiple))
    #displaying the final output
    print(10**(power+1),'            ',Monte_Carlo(a,b,f,10**(power+1)))
    print('The value of the integral of given function estimated by Monte Carlo method:',Monte_Carlo(a,b,f,10**(power+1)))
            
main()      
'''
#Output
Calculating the integral of given function by Monte Carlo method for various values of N:
The value of the integral of given function estimated by Monte Carlo method:3.1410222222222224
'''
