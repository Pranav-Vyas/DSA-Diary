'''
You are given a graph with n vertices and m edges.

You can remove one edge from anywhere and add that edge between any two vertices in one operation.

Find the minimum number of operations that will be required to make the graph connected.

If it is not possible to make the graph connected, return -1.
'''

class Solution:
    def Solve(self, n, adj):
        if len(adj) < n-1: # edges should be atleast n-1 for a connected graph
            return -1
        rank = [0 for _ in range(n)]
        parent = [i for i in range(n)]
        
        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]
        
        def union(u,v):
            pu = find(u)
            pv = find(v)
            if pu == pv:
                return
            if rank[pu] > rank[pv]:
                parent[pv] = pu
            if rank[pu] < rank[pv]:
                parent[pu] = pv
            else:
                parent[pv] = pu
                rank[pu] += 1
        
        for u,v in adj:
            union(u,v)
        
        count = 0
        for i,u in enumerate(parent):
            if i == u:
                count += 1
        
        return count-1