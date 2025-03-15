n=int(input("enter n:"))

i=1
fact=0
while(fact<n):
  fact=fact*i
  i=i+1

  if (fact==n):
    print(1)

  else:
    print(0)