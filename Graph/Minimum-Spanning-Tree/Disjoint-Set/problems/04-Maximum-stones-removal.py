# problem - https://practice.geeksforgeeks.org/problems/maximum-stone-removal-1662179442/1

class Solution:
    def maxRemove(self, adj, n):
        maxRow = 0
        maxCol = 0
        for u,v in adj:
            maxRow = max(maxRow,u)
            maxCol = max(maxCol,v)
        parent = [i for i in range(maxRow+maxCol+2)]
        size = [1 for i in range(maxRow+maxCol+2)]
        
        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]
            
        def union(u,v):
            pu = find(u)
            pv = find(v)
            if pu == pv:
                return
            if size[pu] > size[pv]:
                parent[pv] = pu
                size[pu] += size[pv]
            else:
                parent[pu] = pv
                size[pv] += size[pu]
            
        stonesNode = set()
        for u,v in adj:
            nodeRow = u
            nodeCol = v+maxRow+1
            union(nodeRow, nodeCol)
            stonesNode.add(nodeRow)
            stonesNode.add(nodeCol)
        
        count = 0
        for s in stonesNode:
            if s == find(s):
                count += 1
                
        return n-count