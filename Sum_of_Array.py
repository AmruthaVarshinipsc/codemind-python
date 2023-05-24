n=int(input())
arr=list(map(int,input().split()))
Sum = 0

for i in range(n):
   Sum = Sum + arr[i]
print (Sum)