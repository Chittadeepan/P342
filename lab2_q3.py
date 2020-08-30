#reading matrix M from Matrix_M_lab2.txt
with open("Matrix_M_lab2.txt") as fptr:
       data=fptr.read()
print('M:')
print(data)
x=data.split()
print('\n')
#reading matrix N from Matrix_N_lab2.txt
with open("Matrix_N_lab2.txt")  as  fpt:
      data=fpt.read()
print('N:')
print(data)
y=data.split()
print('\n')
#calling eval function for elements of a and storing them in a using for loop
for index in range(len(x)):
      x[index]=eval(x[index])
#calling eval function for elements of b and storing them in b using for loop
for index in range(len(y)):
      y[index]=eval(y[index])
#initialising  M as 2 dimensional list 
#storing the elements of x in M 
M=[ [x[0],x[1],x[2]], [x[3],x[4],x[5]], [x[6],x[7],x[8]] ]
#initialising N as 2 dimensional list 
#storing the elements of y in N 
N=[ [y[0],y[1],y[2]], [y[3],y[4],y[5]], [y[6],y[7],y[8]] ]
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
#Output:
M:
4  -6  8
3  7  -2
-5  0  17



N:
-5  2  -13
0  17  6
4  10  -2



M×N:
12        -14        -104
-23        105        7
93        160        31



M×A:
98
-55
92
 
'''             
