#initialising sum, number and index
sum=0
number=0.001
index=1
# assigning 1/number to a variable n to get the input for the last index of while loop
n=1/number
#displaying the last index of while loop after asking for input from terminal
print('Asking for input from terminal for performing the required sum:',n)
#using while loop to find sum
while index<=n:
      sum=sum+1/index
      index+=1
#displaying output
print('\nSumming over 1 + 1/2 + 1/3...  till sum does not change by more than 0.001 :',sum)
print('\n\n')