#include<stdio.h>
#include<stdlib.h>
int main()
{
    //initialising distance and count
    float distance=0;
    float count=0;


    //using for loop for traversing the number of discrete points (N=6) points along horizontal direction 
    for (int x1=0;x1<6;x1++){
            //using another for loop to consider the distance of other  discrete points from each fixed discrete point along horizontal direction 
            for (int x2=0;x2<6;x2++){
                 //using for loop for traversing the number of discrete points (N=6) points along vertical direction
                 for (int y1=0;y1<6;y1++){
                       //using another for loop to consider the distance of other  discrete points from each fixed discrete point
                       for (int y2=0;y2<6;y2++){
                             //calculating the distance of any two discrete points in 6 by 6 two dimensional grid                
                             distance=distance+abs(x2-x1)+ abs(y2-y1);
                            //calculating the total number of cases 
                             count+=1;
                       }
                 }
            }
    }
        
                
            

    //initialising average distance      
    float average_distance=distance/count;
    //displaying the total distance between any two discrete points   
    printf("Total distance between any two discrete point:%f\n\n",distance);
    //displaying the total number of  cases for calculating distance between any two discrete point
    printf("Total number of cases for calculating distance between any two discrete point: %f\n\n",count);
    //displaying the average distance between any two discrete points
    printf("The average distance between any two discrete points:%f\n\n ",average_distance);
    return 0;
}
/*
//Output
Total distance between any two discrete point:5040.000000

Total number of cases for calculating distance between any two discrete point: 1296.000000

The average distance between any two discrete points:3.888889
*/
