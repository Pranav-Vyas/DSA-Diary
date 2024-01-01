
'''
Source = 0
Find shortest path for all nodes from source.

problem - https://practice.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1
'''

class Solution:
    def shortestPath(self, n, m, edges):
        graph = [[] for _ in range(n)]
        visited = [False for _ in range(n)]
        topo = []
        for u,v,w in edges:
            graph[u].append((v,w))
        def dfs(u):
            visited[u] = False
            for v,w in graph[u]:
                if not visited[v]:
                    dfs(v)
            topo.append(u)
        for u in range(n):
            if not visited[u]:
                dfs(u)
        ans = [float('inf') for _ in range(n)]
        ans[0] = 0
        visited = [False for _ in range(n)]
        while topo:
            node = topo.pop()
            for u,w in graph[node]:
                ans[u] = min(ans[u], ans[node] + w)
        for i,w in enumerate(ans):
            if w == float('inf'):
                ans[i] = -1
        return ans