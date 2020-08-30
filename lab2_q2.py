#creating vector A
A=[2,-7,6]
#displaying vector A
print('A:',A)
#creating vector B
B=[3,2 ,-7]
#displaying vector B
print('B:',B)
#initialising sum
sum=0
#calculating sum of A and B by list comprehension mechanism 
A_add_B=[A[i]+B[i] for i in range(len(A))]
#displaying vector addition
print('A+B:',A_add_B)      
#scalar dot product using for loop 
for index in range(len(A)):
      sum=sum+A[index]*B[index]
#storing sum in A_dot_B      
A_dot_B=sum
#displaying dot product
print('A.B:',A_dot_B)    
''' 
# Output
A: [2, -7, 6]
B: [3, 2, -7]
A+B: [5, -5, -1]
A.B: -50
'''