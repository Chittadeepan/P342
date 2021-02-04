#importing everything from library
from library import *
#importing everything from math module
from math import *
def main():
    #initialising number of observations
    N=12
    #calling matrix_read_and_write method for reading the dat file
    matrix_read_and_write("esem_table.dat","")
    
    
    #data points for two sets of equations
    A=[[0,2.20],[0.30,1.96],[0.60,1.72],[0.90,1.53],[1.20,1.36],[1.50,1.22],[1.80,1.10],[2.10,1.00],[2.40,0.86],[2.70,0.75],[3.00,0.65],[3.30,0.60]]
    B=[[0,log(2.20)],[0.30,log(1.96)],[0.60,log(1.72)],[0.90,log(1.53)],[1.20,log(1.36)],[1.50,log(1.22)],[1.80,log(1.10)],[2.10,log(1.00)],[2.40,log(0.86)],[2.70,log(0.75)],[3.00,log(0.65)],[3.30,log(0.60)]]  
    
    #part(i) omega(t)=omega_0 + omega_c*t
    
    #calling least_square_fitting_method to determine slope,intercept and quality of fit
    slope_1,intercept_1,r_1=least_square_fitting(N,A)
    print("\nFrom the obtained value of slope and intercept, the value of omega_0:",intercept_1," and the value of omega_c:",slope_1,"and the quality of fit",r_1**2,".")

    #part(ii) omega(t)=omega_0*e**(-omega_c*t). This implies ln(omega(t))=ln(omega_0)-omega_c*t

    #calling least_square_fitting_method to determine slope,intercept and quality of fit
    slope_2,intercept_2,r_2=least_square_fitting(N,B)
    print("\nFrom the obtained value of slope and intercept, the value of omega_0:",e**intercept_2," and the value of omega_c:",-slope_2,"and the quality of fit",r_2**2,".")       
main()
'''
#output
#time   angular velocity
#
0.00    2.20
0.30    1.96
0.60    1.72
0.90    1.53
1.20    1.36
1.50    1.22
1.80    1.10
2.10    1.00
2.40    0.86
2.70    0.75
3.00    0.65
3.30    0.60


Total number of observations: 12
Time: 0
Angular velocity: 2.2


Time: 0.3
Angular velocity: 1.96


Time: 0.6
Angular velocity: 1.72


Time: 0.9
Angular velocity: 1.53


Time: 1.2
Angular velocity: 1.36


Time: 1.5
Angular velocity: 1.22


Time: 1.8
Angular velocity: 1.1


Time: 2.1
Angular velocity: 1.0


Time: 2.4
Angular velocity: 0.86


Time: 2.7
Angular velocity: 0.75


Time: 3.0
Angular velocity: 0.65


Time: 3.3
Angular velocity: 0.6


S_xx: 12.86999999999999
S_yy: 2.9882916666666652
S_xy: -6.109500000000001

Slope: -0.4747086247086251
Intercept: 2.0291025641025646

Pearson's r: 0.9851557666128388

From the obtained value of slope and intercept, the value of omega_0: 2.0291025641025646  and the value of omega_c: -0.4747086247086251 and the quality of fit 0.9705318844905301 .
Total number of observations: 12
Time: 0
Angular velocity: 0.7884573603642703


Time: 0.3
Angular velocity: 0.6729444732424258


Time: 0.6
Angular velocity: 0.5423242908253617


Time: 0.9
Angular velocity: 0.4252677354043441


Time: 1.2
Angular velocity: 0.3074846997479607


Time: 1.5
Angular velocity: 0.19885085874516517


Time: 1.8
Angular velocity: 0.09531017980432493


Time: 2.1
Angular velocity: 0.0


Time: 2.4
Angular velocity: -0.15082288973458366


Time: 2.7
Angular velocity: -0.2876820724517809


Time: 3.0
Angular velocity: -0.4307829160924542


Time: 3.3
Angular velocity: -0.5108256237659907


S_xx: 12.86999999999999
S_yy: 2.0176656494342344
S_xy: -5.091322766439923

Slope: -0.3955961745485569
Intercept: 0.7902775293458725

Pearson's r: 0.9991179387307727

From the obtained value of slope and intercept, the value of omega_0: 2.2040080182882558  and the value of omega_c: 0.3955961745485569 and the quality of fit 0.9982366554936281 .
'''
