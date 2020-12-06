#importing everything from math module 
from math import *
#importing all functions from library
from library import *
#1st coupled differential equation
def f_1(z):
    p = z
    return p
#2nd coupled differential equation
def f_2(x,y,z):
    p = z+1
    return p
#main program
def main():
    #initialising the values of x, y, intervals, ranges for x and y and estimated slopes
    x_0=0
    y_0=0
    h=0.01
    x_n=1
    y_n=3.43656
    z_1=1.5
    z_2=2.5
    print("\nThe slope at x=",x_0,"is estimated as:",z_1)
    print("\nThe slope at x=",x_n,"is estimated as:",z_2)
    print("\nSolving the given differential equation via shooting method:")
    #calling shooting method with initial values obtained above and both the functions as parameters and storing the final values of Y and the calculated slope in y and z
    y,z=shooting_method(x_0,y_0,h,x_n,y_n,z_1,z_2,f_1,f_2)
    #displaying the values of y and z
    print("\nFinal value of Y:",y,"and calculated slope:",z)
main()
'''
#Output

The slope at x= 0 is estimated as: 1.5

The slope at x= 1 is estimated as: 2.5

Solving the given differential equation via shooting method:

Final value of Y: 3.436560000000001 and calculated slope: 1.5853645524811115

'''
