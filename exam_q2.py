#importing everything from library
from library import *
#importing everything from math module
from math import *
#f(phi) function
def f(phi):
    #initialising parameters of simple pendulum as L,theta,g,a according to the given set of values
    L=1
    theta_m=pi/4
    g=9.8
    a=sin(theta_m/2)
    #function to determine time period
    T=4*sqrt(L/g)*(1/sqrt(1-a**2*sin(phi)**2))

    return T

#main program
def main():
    #initialising limits of integration
    a=0
    b=pi/2
    N=10
    #calling simpson method to find the integration result
    result=Simpson(a,b,f,N)
    print("Number of steps       Result")
    print("     ",N,"           ",result)
main()
'''
#output
Number of steps       Result
      10             2.0873200174795916
'''
