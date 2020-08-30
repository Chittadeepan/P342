#initialising distance and count
distance=0
count=0


#using for loop for traversing the number of discrete points (N=6) points along horizontal direction 
for x1 in range(0,6):
            #using another for loop to consider the distance of other  discrete points from each fixed discrete point along horizontal direction 
            for x2 in range(0,6):
                 #using for loop for traversing the number of discrete points (N=6) points along vertical direction
                 for y1 in range(0,6):
                       #using another for loop to consider the distance of other  discrete points from each fixed discrete point
                       for y2 in range(0,6):
                             #calculating the distance of any two discrete points in 6 by 6 two dimensional grid                
                             distance=distance+abs(x2-x1)+ abs(y2-y1)
                            #calculating the total number of cases 
                             count+=1
       
average_distance=distance/count
#displaying the total distance between any two discrete points   
print("Total distance between any two discrete point:",distance)
print('\n')
#displaying the total number of  cases for calculating distance between any two discrete point
print("Total number of cases for calculating distance between any two discrete point: ",count)
print('\n')
#displaying the average distance between any two discrete points
print("The average distance between any two discrete points: ",average_distance)
'''
 #Output
 Total distance between any two discrete point: 5040


Total number of cases for calculating distance between any two discrete point:  1296


The average distance between any two discrete points:  3.888888888888889
'''