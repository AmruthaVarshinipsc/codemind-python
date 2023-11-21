n=int(input())
if n<4:
    print("1")
elif (n%4==0):
    print(n//4)
else:
    print((n//4)+1)