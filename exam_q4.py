#importing everything from library
from library import *
#importing everything from math module
from math import *
#1st f(x) coupled equation
def f_1(z):
    a=z
    return a
#2nd f(x) coupled equation
def f_2(x,y,z):
    #initialising value of g
    g=9.8
    
    a=-g
    return a
#main program
def main():
    #initialising initial time,y_displacement,final time,final y_displacement,step size and two guessed slopes
    t_0=0
    t_n=5
    y_0=2
    y_n=45
    h=0.1
    z_1=-9.8
    z_2=-5
    #calling shooting method to solve given boundary value problem
    
    shooting_method(t_0,y_0,h,t_n,y_n,z_1,z_2,f_1,f_2)
    print("\nThe launch velocity determination depends on guess of slope at initial and final positions which can be calculated by hand")
main()
    
