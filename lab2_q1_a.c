#include<stdio.h>
#include<stdlib.h>
int main(){
    // initialising distance and count
    float distance=0;
    float count=0;
    //using for loop for traversing the number of discrete points (N=6) points
    for (int i=0;i<6;i++){
       //using another for loop to calculate the distance of other  discrete points from each fixed discrete point
       for (int j=0;j<6;j++){
            distance=distance+abs(j-i);
            //calculating the number of cases
            count+=1;
       }
    }
    //initialising average_distance
    float average_distance=(distance/count);        
    //displaying the total distance between any two discrete points   
    printf("Total distance between any two discrete point:%f\n\n",distance);
    //displaying the total number of  cases for calculating distance between any two discrete point
    printf("Total number of cases for calculating distance between any two discrete point:%f\n\n",count);
    //displaying the average distance between any two discrete points
    printf("The average distance between any two discrete points:%f\n\n ",average_distance);
    return 0; 
}
/*
//Output
Total distance between any two discrete point:70.000000

Total number of cases for calculating distance between any two discrete point:36.000000

The average distance between any two discrete points:1.944444
*/
