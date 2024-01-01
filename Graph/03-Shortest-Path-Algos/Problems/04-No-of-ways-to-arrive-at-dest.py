'''
problem - https://practice.geeksforgeeks.org/problems/number-of-ways-to-arrive-at-destination/1
'''

from typing import List
from heapq import *

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        for u,v,d in roads:
            graph[u].append((v,d))
            graph[v].append((u,d))
        pq = []
        dist = [float('inf') for _ in range(n)]
        ways = [0 for _ in range(n)]
        dist[0] = 0
        ways[0] = 1
        pq.append((0,0))
        while pq:
            d,u = heappop(pq)
            for neig,w in graph[u]:
                if w+d < dist[neig]:
                    dist[neig] = w+d
                    ways[neig] = ways[u]
                    heappush(pq,(dist[neig],neig))
                elif w+d == dist[neig]:
                    ways[neig] += ways[u]
        return ways[n-1] % 1000000007