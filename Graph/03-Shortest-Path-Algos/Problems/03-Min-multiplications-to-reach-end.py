'''
problem - https://practice.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1

Given start, end and an array arr of n numbers. 
At each step, start is multiplied with any number in the array 
and then mod operation with 100000 is done to get the new start.
Your task is to find the minimum steps in which end can be achieved starting from start.
'''

# Dijkstra's algo with queue not PQ

from typing import List
from collections import deque
 
class Solution:
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        dist = [float('inf') for _ in range(100000)]
        dist[start] = 0
        q = deque()
        q.append((start,0))
        while q:
            num,steps = q.popleft()
            for x in arr:
                newNum = (num * x) % 100000
                if steps + 1 < dist[newNum]:
                    dist[newNum] = steps+1
                    if newNum == end:
                        return steps+1
                    q.append((newNum,steps+1))
        if dist[end] == float('inf'):
            return -1
        return dist[end]