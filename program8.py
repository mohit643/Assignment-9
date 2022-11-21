# Write a python script to print squares of first N natural numbers
i=int(input("enter a no "))
j=int(input("maximum "))
while j>=i:
  if i%2==0:
    print(i**2)
    i+=1
  else:
    i+=1  