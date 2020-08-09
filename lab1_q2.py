#user input
n=int(input('Enter an integer whose factorial you want:'))
#initialising fact and index
fact=1
index=2
#checking boundary conditions
if n>=0:
      #calculating factorial in while loop
      while index<=n:
            fact=fact*index
            index+=1
      #display output
      print ('\nThe factorial of',n,':',fact)
#checking boundary conditions
else:
       print('\nThe given input is a not a positive integer!')
print('\n\n')