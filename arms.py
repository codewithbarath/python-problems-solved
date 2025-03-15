n=123
first_dig=(n//100)
second_dig=(n//10)%10
third_dig=n%10


arms=(first_dig**3)+(second_dig**3)+(third_dig**3)
print(arms)
