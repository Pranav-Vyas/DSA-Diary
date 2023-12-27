
# problem - https://practice.geeksforgeeks.org/problems/cheapest-flights-within-k-stops/1

from collections import deque

class Solution:
    def CheapestFLight(self,n,flights,src,dest,k):
        graph = [[] for _ in range(n)]
        for u,v,c in flights:
            graph[u].append((v,c))
        q = deque()
        dist = [float('inf') for _ in range(n)]
        dist[src] = 0
        q.append((0,src,0))
        while q:
            stops,node,cost = q.popleft()
            if stops > k:
                break
            for neig, w in graph[node]:
                if cost+w < dist[neig]:
                    dist[neig] = cost+w
                    q.append((stops+1, neig, cost+w))
        if dist[dest] == float('inf'):
            return -1
        return dist[dest]
