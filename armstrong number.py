def febono(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return febono(n-1)+febono(n-2)
    

n=5
print(febono(n))