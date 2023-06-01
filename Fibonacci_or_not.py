from math import sqrt
def solve(n):
   phi = 0.5 + 0.5 * 5.0**0.5
   a = phi * n
   return n == 0 or abs(round(a) - a) < 1.0 / n

n = int(input())
print(solve(n))