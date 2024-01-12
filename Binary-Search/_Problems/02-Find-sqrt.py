# Find square root of a number using binary search

def floorSqrt(n):
   if n == 1:
      return n
   i = 1
   j = n//2
   ans = n
   while i <= j:
      m = (i+j)//2
      if m*m <= n:
         ans = m
         i = m+1
      else:
         j = m-1
   return ans

n= int(input())
print(floorSqrt(n))