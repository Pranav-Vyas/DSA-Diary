'''
Find shortest path for all nodes in an undirected graph.
Weight of all edges is 1

problem - https://practice.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1
'''

from collections import deque

class Solution:
    def shortestPath(self, edges, n, m, src):
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        ans = [float("inf") for _ in range(n)]
        ans[src] = 0
        q = deque()
        q.append((src,0))
        while q:
            u,w = q.popleft()
            for v in graph[u]:
                if ans[u] + 1 < ans[v]:
                    ans[v] = ans[u] + 1
                    q.append((v,ans[v]))
        for i,w in enumerate(ans):
            if w == float("inf"):
                ans[i] = -1
        return ans