#importing everything from library
from library import *
#importing everything from math module
from math import *

#function with specifications of ellipsoid
def f(x,y,z):
    #parameters
    a=1.0
    b=1.5
    c=2.0
    #equation
    A=x**2/a**2 + y**2/b**2 + z**2/c**2
    return A
#main program
def main():
    count=1
    #calculating volume of ellipsoid for different values of N
    print("Number of trials       N       Volume of ellipsoid")
    for N in range(100,28000,3000):
        Volume=monte_carlo_volume(-1,-1.5,-2.0,1,1.5,2.0,f,N)
        print("      ",count,"            ",N,"       ",Volume)
        count+=1
main()
'''
#Output
Number of trials       N       Volume of ellipsoid
       1              100         11.52
       2              3100         12.270967741935483
       3              6100         12.204590163934427
       4              9100         12.582857142857142
       5              12100         12.640661157024795
       6              15100         12.569006622516557
       7              18100         12.519779005524864
       8              21100         12.434502369668246
       9              24100         12.611452282157675
       10              27100         12.457859778597786

'''
