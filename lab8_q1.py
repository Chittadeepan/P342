#importing everything from library
from library import *
#importing everything from math module
from math import *
#main program

def main():
    #initializing initial position of random walker and total number of random walks

    x_0=0.00
    y_0=0.00
    walk_range=100

    
    #calling random walk function with different number of steps,initial position and walk_range as parameters

    random_walk(x_0,y_0,250,walk_range,"Data for Random_Walk for 250 steps.txt")#step_range=250
    
    random_walk(x_0,y_0,500,walk_range,"Data for Random_Walk for 500 steps.txt")#step_range=500
    
    random_walk(x_0,y_0,750,walk_range,"Data for Random_Walk for 750 steps.txt")#step_range=750
    
    random_walk(x_0,y_0,1000,walk_range,"Data for Random_Walk for 1000 steps.txt")#step_range=1000
    
    random_walk(x_0,y_0,1250,walk_range,"Data for Random_Walk for 1250 steps.txt")#step_range=1250
    

    
main()    
'''
#Output
After 250 number of steps starting from ( 0.0 , 0.0 ) and 20 random walks, the final position of random walker:( -0.9720367549877376 , -6.773192939045486 ) and the radial distance R= 4.827242944614464  .
After 250 number of steps starting from ( 0.0 , 0.0 ) and 40 random walks, the final position of random walker:( 7.89618729025573 , -1.5500117099375144 ) and the radial distance R= 24.261212184769402  .
After 250 number of steps starting from ( 0.0 , 0.0 ) and 60 random walks, the final position of random walker:( 17.602286405164172 , 1.1618905737122318 ) and the radial distance R= 10.880358832474949  .
After 250 number of steps starting from ( 0.0 , 0.0 ) and 80 random walks, the final position of random walker:( 14.227604587155607 , 19.2919320454697 ) and the radial distance R= 7.188289172370994  .
After 250 number of steps starting from ( 0.0 , 0.0 ) and 100 random walks, the final position of random walker:( -0.6769992126353412 , 5.9012736824548995 ) and the radial distance R= 9.040155202385813  .

After  100  number of random walks, RMS distance= 14.461103173135944 , average displacement along x-axis= -0.006769992126353413 , average displacement along y-axis= 0.059012736824548995 .



After 500 number of steps starting from ( 0.0 , 0.0 ) and 20 random walks, the final position of random walker:( 14.036438109536597 , -22.867310028051783 ) and the radial distance R= 12.378283355849415  .
After 500 number of steps starting from ( 0.0 , 0.0 ) and 40 random walks, the final position of random walker:( 2.0782735877561387 , 0.7725606068377159 ) and the radial distance R= 43.96569957424637  .
After 500 number of steps starting from ( 0.0 , 0.0 ) and 60 random walks, the final position of random walker:( -10.04316674438572 , -4.425442373590962 ) and the radial distance R= 3.62069311181369  .
After 500 number of steps starting from ( 0.0 , 0.0 ) and 80 random walks, the final position of random walker:( -7.330725390302158 , -4.028402897065016 ) and the radial distance R= 8.725566523092935  .
After 500 number of steps starting from ( 0.0 , 0.0 ) and 100 random walks, the final position of random walker:( 23.946247482120533 , -9.390966837005177 ) and the radial distance R= 14.713570543134376  .

After  100  number of random walks, RMS distance= 23.4863716152814 , average displacement along x-axis= 0.23946247482120533 , average displacement along y-axis= -0.09390966837005177 .



After 750 number of steps starting from ( 0.0 , 0.0 ) and 20 random walks, the final position of random walker:( -3.5274680833686753 , 7.907713909627612 ) and the radial distance R= 34.34706782164327  .
After 750 number of steps starting from ( 0.0 , 0.0 ) and 40 random walks, the final position of random walker:( -28.60284824979087 , -28.140016769610224 ) and the radial distance R= 18.023909314144078  .
After 750 number of steps starting from ( 0.0 , 0.0 ) and 60 random walks, the final position of random walker:( -0.31320878085661874 , -25.763243827728342 ) and the radial distance R= 18.822597112796718  .
After 750 number of steps starting from ( 0.0 , 0.0 ) and 80 random walks, the final position of random walker:( 15.671876103632007 , 5.813369040097824 ) and the radial distance R= 24.922955467347712  .
After 750 number of steps starting from ( 0.0 , 0.0 ) and 100 random walks, the final position of random walker:( 6.067052638625093 , 1.4900555829981812 ) and the radial distance R= 8.484168399941106  .

After  100  number of random walks, RMS distance= 25.58665319209774 , average displacement along x-axis= 0.06067052638625093 , average displacement along y-axis= 0.014900555829981812 .



After 1000 number of steps starting from ( 0.0 , 0.0 ) and 20 random walks, the final position of random walker:( -13.846141601363351 , 15.380632883854647 ) and the radial distance R= 19.484771130606156  .
After 1000 number of steps starting from ( 0.0 , 0.0 ) and 40 random walks, the final position of random walker:( 18.5119929464547 , -38.80785453154255 ) and the radial distance R= 17.39073166432471  .
After 1000 number of steps starting from ( 0.0 , 0.0 ) and 60 random walks, the final position of random walker:( 14.13676674480089 , 8.225787414230865 ) and the radial distance R= 86.74736769899224  .
After 1000 number of steps starting from ( 0.0 , 0.0 ) and 80 random walks, the final position of random walker:( -13.46711338138048 , 27.652797369253328 ) and the radial distance R= 24.501979420248436  .
After 1000 number of steps starting from ( 0.0 , 0.0 ) and 100 random walks, the final position of random walker:( 13.964988786845371 , 15.171398653093611 ) and the radial distance R= 44.1113841680325  .

After  100  number of random walks, RMS distance= 31.328315417266374 , average displacement along x-axis= 0.1396498878684537 , average displacement along y-axis= 0.15171398653093612 .



After 1250 number of steps starting from ( 0.0 , 0.0 ) and 20 random walks, the final position of random walker:( 6.662723633649417 , 1.9659109557409662 ) and the radial distance R= 40.83208126838498  .
After 1250 number of steps starting from ( 0.0 , 0.0 ) and 40 random walks, the final position of random walker:( 39.63086088942172 , -24.4344141968454 ) and the radial distance R= 38.74579185865816  .
After 1250 number of steps starting from ( 0.0 , 0.0 ) and 60 random walks, the final position of random walker:( -45.79752180641832 , -3.71094364339545 ) and the radial distance R= 25.93987615603073  .
After 1250 number of steps starting from ( 0.0 , 0.0 ) and 80 random walks, the final position of random walker:( -56.980747297435464 , -12.152444452046904 ) and the radial distance R= 38.139758747146374  .
After 1250 number of steps starting from ( 0.0 , 0.0 ) and 100 random walks, the final position of random walker:( -7.619475553985626 , -30.24804850335051 ) and the radial distance R= 62.92054027413432  .

After  100  number of random walks, RMS distance= 33.25228916046043 , average displacement along x-axis= -0.07619475553985626 , average displacement along y-axis= -0.3024804850335051 .



'''
