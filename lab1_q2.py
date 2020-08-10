#user input
n=int(input('Enter an integer whose factorial you want:'))
#initialising fact and index
fact=1
index=2
#checking for positive integers 
if n>0:
      #calculating factorial in while loop
      while index<=n:
            fact=fact*index
            index+=1
      #displaying output
      print ('\nThe factorial of',n,':',fact)
#checking boundary conditions
#base case
elif n==0:
      print('\nThe factorial of',n,':',fact)
#checking boundary conditions
else:
       print('\nThe given input is a not a non-negative integer!')
print('\n\n')