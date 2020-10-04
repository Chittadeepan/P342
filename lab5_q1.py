#importing everything from math module 
from math import *
#importing all functions from library
from library import *
#f(x) function
def f(x,choice):
    if choice==1:
        y1=log(x)-sin(x) 
        return y1
    elif choice==2:
        y2=-x-cos(x)
        return y2
#main program
def main():
    
    epsilon=10**(-6)
    a=1.5
    b=2.5
    x_0=1.5
    
    #solving log(x)-sin(x)=0
    #calling Bisection function and displaying the roots obtained
    print('Solving log(x)-sin(x)=0 by Bisection Method:\n')
    root=Bisection(a,b,epsilon,f,1)
    print('Root obtained:',root,'\n')
    
    #calling Regula_Falsi function and displaying the roots obtained
    print('Solving log(x)-sin(x)=0 by Regula_Falsi Method:\n')
    root=Regula_Falsi(a,b,epsilon,f,1)
    print('Root obtained:',root,'\n')

    #calling Newton_Raphson function and displaying the roots obtained
    print('Solving log(x)-sin(x)=0 by Newton_Raphson Method:\n')
    root=Newton_Raphson(x_0,epsilon,f,1)
    print('Root obtained:',root,'\n')
    
    #solving -x-cos(x)=0
    #calling Bisection function and displaying the roots obtained
    print('Solving -x-cos(x)=0 by Bisection Method:\n')
    root=Bisection(a,b,epsilon,f,2)
    print('Root obtained:',root,'\n')
    
    #calling Regula_Falsi fuinction and displaying the roots obtained
    print('Solving -x-cos(x)=0 by Regula_Falsi Method:\n')
    root=Regula_Falsi(a,b,epsilon,f,2)
    print('Root obtained:',root,'\n')
    
    #calling Newton_Raphson function and displaying the roots obtained
    print('Solving -x-cos(x)=0 by Newton_Raphson Method:\n')
    root=Newton_Raphson(0.5,epsilon,f,2)#initial guess=0.5
    print('Root obtained:',root,'\n')
    
    
main()
'''
#Output
Solving log(x)-sin(x)=0 by Bisection Method:
      
Root obtained: 2.219106674194336

Solving log(x)-sin(x)=0 by Regula_Falsi Method:
      
Root obtained: 2.2191071418525734

Solving log(x)-sin(x)=0 by Newton_Raphson Method:
      
Root obtained: 2.2191071489137406

Solving -x-cos(x)=0 by Bisection Method:
      
Root obtained: -0.7390855252742767

Solving -x-cos(x)=0 by Regula_Falsi Method:
      
Root obtained: -0.7390851331785756

Solving -x-cos(x)=0 by Newton_Raphson Method:
      
Root obtained: -0.7390851332144047
'''

