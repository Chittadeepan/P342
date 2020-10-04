#importing everything from math module 
from math import *
#importing all functions from library
from library import *
#poly_f(x) function
def poly_f(x,coeff,n):
    sum=0
    for i in range(1,n+1):
        sum=sum+coeff[i-1]*x**(n-i)
    
    return sum
#main program
def main():
    
    #initialising final absolute error(epsilon), initial guess of root(root) and number of terms in polynomial(n)
    epsilon=10**(-6)
    root=0.9
    n=5
    
    #initialising coeff list and appending coeff elements corresponding to their variables with decreasing power
    coeff=[1,-3,-7,27,-18]
    
    #solving P(x)=x^4-3x^3-7x^2+27x-18
    print('Solving x^(4)-3x^(3)-7x^(2)+27x-18 by Laguerre method and Synthetic Division method:')
    
    #calling Laguerre function and Synthetic Division function and displaying the roots obtained in a loop
    for index in range(n,1,-1):
        root=Laguerre(root,epsilon,coeff,index,poly_f)
        if index>0:
            coeff=Synthetic_Division(root,coeff)
        print('One of the roots obtained:',round(root,6))
main()
'''
#Output
Solving x^(4)-3x^(3)-7x^(2)+27x-18 by Laguerre method and Synthetic Division method:
One of the roots obtained: 1.0
One of the roots obtained: 2.0
One of the roots obtained: 3.0
One of the roots obtained: -3.0
'''
