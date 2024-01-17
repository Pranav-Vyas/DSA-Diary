# https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1

'''
Given a row wise sorted matrix of size R*C where R and C are always odd, find the median of the matrix.
'''

class Solution:
  def median(self, mat, R, C):
    def upper_bound(i,tar):
      ans = C
      low = 0
      high = C-1
      while low <= high:
        m = (low+high)//2
        if mat[i][m] <= tar:
          low = m+1
        else:
          ans = m
          high = m-1
      return ans
    def calcSmallEqual(tar):
      count = 0
      for i in range(R):
        count += upper_bound(i,tar)
      return count
    low = float("inf")
    high = -float("inf")
    req = (R*C)//2
    for i in range(R):
      low = min(low,mat[i][0])
      high = max(high,mat[i][-1])
    while low <= high:
      m = (low+high)//2
      count = calcSmallEqual(m)
      if count <= req:
        low = m+1
      else:
        high = m-1
    return low