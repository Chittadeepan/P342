#reading matrix M from Matrix_M.txt
with open("Matrix_M.txt") as fptr:
       data=fptr.read()
print('M:')
print(data)
x=data.split()
print('\n')
#reading matrix N from Matrix_N.txt
with open("Matrix_N.txt")  as  fpt:
      data=fpt.read()
print('N:')
print(data)
y=data.split()
print('\n')

#initialising  M as 2 dimensional list 
#storing the elements of x in M by list comprehension mechanism 
M=[[eval(x[i]) for i in range(0,3)], [eval(x[i]) for i in range(3,6)], [eval(x[i]) for i in range(6,9)] ]
#initialising N as 2 dimensional list 
# storing the elements of y in N by list comprehension mechanism 
N=[[eval(y[i]) for i in range(0,3)], [eval(y[i]) for i in range(3,6)], [eval(y[i]) for i in range(6,9)] ]
#initialising A as a 2 dimensional list
A=[[2],[-7],[6]]
#calculating M×N
#declaring MxN as empty list
MxN=[]

#using for loop for traversing the number of rows in M×N
for k in range (0,len(M)):
      #initialising  a as an empty list
      a=[]
      #initialising l as the number of elements in M[k]
      l=len(M[k])
      #using another for loop for traversing the number of elements in each row of M×N
      for i in range(0,len(N[l-1])):
            #initialising x
            x=0
            #using another for loop to calculate each element in each row of M×N
            for j in range(0,l):
                  x=x+M[k][j]*N[j][i]
            #appending each element in list a     
            a.append(x)
     
       #appending list a within another list M×N
      MxN.append(a)
      
#displaying M×N by using two for loops
print('M×N:')
for i in range(len(MxN)):
      for j in range(len(MxN[i])):
            #checking for last element 
            if j==(len(MxN[i])-1):
                  print(MxN[i][j])
            else:
                  print(MxN[i][j],end='        ')
print('\n\n')
'''
#output: M×N:
12    -14   -104
-23   105    7
93    160    31                
'''
#calculating M×A
#declaring MxA as empty list
MxA=[]

#using for loop for traversing the number of rows in M×A
for k in range (0,len(M)):
      #initialising  b as an empty list
      b=[]
      #using for loop for traversing the number of elements in each row of M×A
      for i in range(0,len(A[i])):
            #initialising y
            y=0
            #using another for loop to calculate each element in each row of M×A
            for j in range(0,len(M[j])):
                  y=y+M[k][j]*A[j][i]
            #appending each element in list b    
            b.append(y)
       #appending list b within another list M×A
      MxA.append(b)
      
#displaying M×A by using two for loops
print('M×A:')
for i in range(len(MxA)):
      for j in range(len(MxA[i])):
            #checking for last element
            if j==(len(MxA[i])-1):
                  print(MxA[i][j])
            else:
                  print(MxA[i][j],end='        ')
'''
#output: M×A:
98
-55
92  
'''             
