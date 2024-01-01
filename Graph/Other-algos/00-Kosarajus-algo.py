
'''  --------------- Strongly Connected Components -------------------- '''

'''
- Every vertex is reachable from every other vertex

  Algo

- find topo sort
- reverse edges of graph
- iterate vertex from topo sort in reverse order and call dfs
- count components
'''

class Solution:
    def kosaraju(self, n, adj):
        stack = []
        visited = [False for _ in range(n)]
        
        def topo(u):
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    topo(v)
            stack.append(u)
            
        def dfs(u):
            visited[u] = True
            for v in revAdj[u]:
                if not visited[v]:
                    dfs(u)
        
        revAdj = [[] for _ in range(n)]
        for u,arr in enumerate(adj):
            for v in arr:
                revAdj[v].append(u)
        
        for u in range(n):
            if not visited[u]:
                topo(u)
        
        visited = [False for _ in range(n)]
        
        count = 0
        while stack:
            u = stack.pop()
            if not visited[u]:
                dfs(u)
                count += 1
        return count