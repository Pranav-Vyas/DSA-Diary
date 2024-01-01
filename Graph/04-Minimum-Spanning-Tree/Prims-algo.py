
''' ---------------- PRIMS ALGORITHM ---------------------'''

from heapq import *
class Solution:
    def spanningTree(self, v, adj):
        pq = []
        pq.append((0,0))
        ans = 0
        visited = [False for _ in range(v)]
        while pq:
            w,u = heappop(pq)
            if visited[u]:
                continue
            ans += w
            visited[u] = True
            for neig,edgeW in adj[u]:
                if not visited[neig]:
                    heappush(pq,(edgeW,neig))
        return ans