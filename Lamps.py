n,k,x,y = map(int, input().split())
if min(x,y) == x:
    print(n*x)
else:
    print((k*x)+(n-k)*y)