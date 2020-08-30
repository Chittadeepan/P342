# initialising distance,count
distance=0
count=0
#using for loop for traversing the number of discrete points (N=6) points
for i in range (0,6):
       #using another for loop to calculate the distance of other  discrete points from each fixed discrete point
       for j in range(0,6):
            distance=distance+abs(j-i)
            #calculating the total number of cases
            count+=1
#initialising average_distance
average_distance= distance/count        
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
Total distance between any two discrete point: 70


Total number of cases for calculating distance between any two discrete point:  36


The average distance between any two discrete points:  1.9444444444444444
'''