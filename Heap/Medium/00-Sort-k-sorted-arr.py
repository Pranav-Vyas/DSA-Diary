'''
Given an array of n elements, 
where each element is at most k away from its target position, you need to sort the array optimally.

n = 7, k = 3
arr[] = {6,5,3,2,8,10,9}
Output: 2 3 5 6 8 9 10
'''

'''
- keep a k-size heap
- put new element and pop min element from heap
'''

from heapq import *
class Solution:
  def nearlySorted(self,arr,n,k):
    pq = []
    ans = []
    for i in range(k+1):
      pq.append(arr[i])
    heapify(pq)
    maxi = heappop(pq)
    ans.append(maxi)
    for i in range(k+1,n):
      heappush(pq,arr[i])
      cur = heappop(pq)
      ans.append(cur)
    while pq:
      cur = heappop(pq)
      ans.append(cur)
    return ans

'''
  Similar Problems

  - Kth largest element in arr
  - Kth smallest element in arr
'''