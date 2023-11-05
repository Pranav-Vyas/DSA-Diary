''' DETECT CYCLE IN DAG '''

# 1. Do the topological sort
# 2. Check if length of topo == 'n'(no of vertices)
# 3. if not equal, cycle exists otherwise no cycle

from collections import deque

class Solution:
    #Function to detect cycle in a directed graph.
    def isCyclic(self, n, adj):
        topo = []
        indeg = [0 for i in range(n)]
        q = deque()
        for arr in adj:
            for x in arr:
                indeg[x] += 1
        for i,d in enumerate(indeg):
            if not d:
                q.append(i)
        while q:
            u = q.popleft()
            topo.append(u)
            for v in adj[u]:
                indeg[v] -= 1
                if not indeg[v]:
                    q.append(v)
        if len(topo) != n:
            return True
        return False