''' --------------  KRUSKALS ALGO ------------------'''

# Disjoint set concept is used here

class Solution:
    def spanningTree(self, V, adj):
        edges = []
        for u in range(V):
            for v,w in adj[u]:
                if v > u:
                    edges.append((w,u,v))
        rank = [0 for i in range(V)]
        parent = [i for i in range(V)]
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
        ans = 0
        edges.sort()
        for w,u,v in edges:
            pu = find(u)
            pv = find(v)
            if pu == pv:
                continue
            union(pu,pv)
            ans += w
        return ans