s=str(input())
digit=0
for ch in s:
   if ch.isdigit():
      digit=digit+1
   else:
      pass
if digit==0:
    print("Doesn't contain digit")
else:
    print("Contains", digit,"digit")