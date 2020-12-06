#importing everything from math module 
from math import *
#importing all functions from library
from library import *
#differential equation (1)
def f_1(x,y):
    z=y*log(y,2.71828)/x
    return z
#differential equation (2)
def f_2(x,y):
    z = 6 - (2*y)/x
    return z
#main program
def main():
    #initialising range and various values of interval for Euler's function
    r=10
    h=0.1
    print("\nSolving differential equation (1):")
    #calculating the solutions of equation (1) using Euler's function in a loop 
    #calling Euler function for equation (1) with initial values of x,y,range,interval and f_1 function as parameters
    x,y=Euler(2,2.71,r,h,f_1)
    print("\nFor differential equation (1), final value of X:",x,"and final value of Y:",y)
    print("\nSolving differential equation (2):")
    #calculating the solutions of equation (2) using Euler's function in a loop
    #calling Euler function for equation (2) with initial values of x,y,range,interval and f_2 function as parameters
    x,y=Euler(3,1,r,h,f_2)
    print("\nFor differential equation (2), final value of X:",x,"and final value of Y:",y) 
main()
'''
#Output

Solving differential equation (1):

For differential equation (1), final value of X: 10.09999999999998 and final value of Y: 127.39874081568563

Solving differential equation (2):

For differential equation (2), final value of X: 10.09999999999998 and final value of Y: 19.789898989898965
'''
