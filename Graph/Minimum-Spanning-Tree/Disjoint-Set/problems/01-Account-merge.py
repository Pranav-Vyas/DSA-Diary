
# problem - https://practice.geeksforgeeks.org/problems/account-merge/1

class Solution:
    def accountsMerge(self, accounts):
        n = len(accounts)
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
        
        name = {}
        for i,arr in enumerate(accounts):
            for j in range(1, len(arr)):
                if arr[j] in name:
                    union(name[arr[j]], i)
                else:
                    name[arr[j]] = i
        
        h = {i:[] for i in range(n)}
        
        for k,v in name.items():
            h[find(v)].append(k)
        
        ans = []
        for k,arr in h.items():
            if arr:
                ans.append([accounts[k][0]])
                ans[-1].extend(sorted(arr))
        return ans