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
    z_1=20
    z_2=40
    #calling shooting method to solve given boundary value problem
    
    y,z=shooting_method(t_0,y_0,h,t_n,y_n,z_1,z_2,f_1,f_2)
    print("\nThe launch velocity is determined from the two guessed slopes to be",z,"m/s.")
main()
'''
#output
From the first guess z_1= 20 the corresponding value of y is obtained as -23.032500000000034  at t= 0.

From the second guess z_2= 40 the corresponding value of y is obtained as 78.96750000000009  at t= 5.

The launch velocity is determined from the two guessed slopes to be 33.33970588235293 m/s.
'''
