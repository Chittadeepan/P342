#initialising sumand index
sum=0
index=1
#using while loop to find sum
while 1/index>=0.001:
      sum=sum+1/index
      index+=1
#displaying output
print('Summing over 1 + 1/2 + 1/3...  till sum does not change by more than 0.001 :',sum)
print('\n\n')