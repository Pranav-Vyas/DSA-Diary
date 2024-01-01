"""
Single source shortest paths for all vertices
"""

# -------------- Method 1 - Queue - Brute force


# -------------- Method 2 - Priority Queue - Greedy
# time - O(ElogV), E = V*V

from heapq import *

class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def dijkstra(self, V, adj, S):
      ans = [float("inf") for _ in range(V)]
      ans[S] = 0
      pq = []
      pq.append((0, S))
      while pq:
        dist, vertex = heappop(pq)
        if dist > ans[vertex]:
          continue
        for v, d in adj[vertex]:
          if dist + d < ans[v]:
            ans[v] = dist + d
            heappush(pq, (ans[v], v))
      return ans

# Print dijkstra path
'''
- maintain a 'parent' array to store from where that node is comming
- then go backwards from parent to parent to get the path
'''