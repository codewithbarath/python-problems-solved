sentence="this problem is an easy problem"
searchword="pro"
new=sentence.split()
print(new)

for index,news in enumerate(new):
    if searchword in news:
        ip=index+1
        print(ip)
        if ip>len(new):
            print(ip)
        else:
            print(-1)

    