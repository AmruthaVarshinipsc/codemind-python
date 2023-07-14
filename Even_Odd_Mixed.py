td=0 
ed=0
od=0
n=int(input())

while n>0:
    d=n%10
    if d%2==0:
        ed=ed+1     # counting the even digits
    elif d%2!=0:
        od=od+1
    td=td+1         # counting the total number of digits
    n=n//10

if td==ed:
    print('Even')
elif td==od:
    print('Odd')
else:
    print('Mixed')