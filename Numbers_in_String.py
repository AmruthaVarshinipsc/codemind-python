x=str(input())
s=0
for i in x:
    if ord(i)>=48 and ord(i)<=57:
        s+=int(i)
print(s)