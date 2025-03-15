a=int(input("enter a:"))
covert_string=str(a)
mirror=(covert_string[::-1])
print(mirror)

square=a**2
num_mirror=int(mirror)
multi_mirror=num_mirror**2

if square==(int(str(multi_mirror)[::-1])):
    print("yes")
else:
    print("no")
