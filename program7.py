# Write a python script to print first N even natural numbers in reverse order

i=int(input("enter a no "))
while i>0:
  if i%2==0:
    print(i)
    i-=1
  else:
    i-=1  