'''
Given an array arr of N integers, the task is to replace each element of the array by its rank in the array. 
The rank of an element is defined as the distance between the element 
with the first element of the array when the array is arranged in ascending order. 
If two or more are same in the array then their rank is also the same as the rank of the first occurrence of the element. 

N = 6
arr = [20, 15, 26, 2, 98, 6]
Output:
4, 3, 5, 1, 6, 2
'''

from heapq import *
class Solution:
    def replaceWithRank(self, n, arr):
        rank = 0
        pre = -1
        pq = []
        pq = [(x,i) for i,x in enumerate(arr)]
        heapify(pq)
        res = [0 for i in range(len(arr))]
        while pq:
            cur,i = heappop(pq)
            if cur == pre:
                res[i] = rank
            else:
                rank += 1
                res[i] = rank
                pre = cur
        return res