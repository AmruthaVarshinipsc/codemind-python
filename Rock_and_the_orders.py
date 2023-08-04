d,c = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if sum(a)<150 and sum(b)<150:
    print("NO")
elif sum(a)>=150 and sum(b)>=150:
    if c<2*d:
        print("YES")
    else:
        print("NO")
else:
    if c<d:
        print("YES")
    else:
        print("NO")