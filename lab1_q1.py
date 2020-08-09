#user input
n= int(input('Enter a natural number upto which you want to get the sum of all its previous numbers: '))
#initialising sum and index
sum=0
index=1
#checking boundary conditions 
if n<1:
      print('\nThe given input is not a natural number!')
else:
      #using while loop to find sum
      while index <= n:
            sum=sum+index
            index+=1
      #displaying output
      print('\nSum of first',n,'natural numbers:',sum)
print('\n\n')