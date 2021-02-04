#importing everything from library
from library import *
#importing everything from math module
from math import *
#f(x) function
def f(x,choice):
    y=(x-5)*e**(x)+5
    
    if choice==1:
        return y
#main program
def main():
    #initialising guess of root,max error,value of h,k and c
    x_0=4.5
    epsilon=0.0001
    h=6.626 * 10**(-34)
    k=1.381 * 10**(-23)
    c=3*10**(8)
    
    #calling Newton_Raphson function to find root
    root=Newton_Raphson(x_0,epsilon,f,1)
    #determining Wien's displacement constant (b)
    b=(h*c)/(k*root)
     
    if root>0:
        print("Root:",root)
        print("Wien's displacement constant (b):",b,"mK")
    else:
        print("Find another root")
main()
'''
#output
No. of iterations     Absolute Error

0                     4.5

1                     0.8888359642872796

2                     0.2964033675230384

3                     0.11272281498411019

4                     0.014381153447536654

5                     0.00021433882835086848

Root: 4.965114231747237
Wien's displacement constant (b): 0.002899010330736563 mK
'''
