#importing everything from math module 
from math import *
#importing all functions from library
from library import *
#first coupled differential equation (dy/dx=z)
def f_1(z):
    a=z
    return a
#second coupled differential equation (d^2 y/dx^2=1-x-dy/dx)
def f_2(x,y,z):
    a=1-x-z
    return a
#main program
def main():
    #initialising the values of x, y, z, intervals and ranges for x
    x_0=0
    y_0=2
    z_0=1
    h=0.1
    H=-0.1
    r=5
    R=-5
    print("\nSolving the given coupled differential equations for positive x:")
    #calling RK4 function with only positive initial values obtained above and both the functions as parameters
    x,y=RK4(x_0,y_0,z_0,h,r,f_1,f_2)
    print("\nFor positive x, final value of X:",x,"and final value of Y:",y)
    print("\nSolving the given coupled differential equations for negative x:")
    #calling RK4 function with positive initial values, negative intervals and ranges obtained above and both the functions as parameters
    x,y=RK4(x_0,y_0,z_0,H,R,f_1,f_2)
    print("\nFor negative x, final value of X:",x,"and final value of Y:",y) 
main()
'''
#Output
Solving the given coupled differential equations for positive x:
For positive x, final value of X: 5.099999999999998 and final value of Y: -1.7566700899695538
Solving the given coupled differential equations for negative x:
For negative x, final value of X: -5.099999999999998 and final value of Y: 135.35010840259812
'''
