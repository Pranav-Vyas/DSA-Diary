from collections import deque

def bfsTraversal(n, adj):
    visited = [False]*n
    ans = []
    q = deque()
    visited[0] = True
    q.append(0)
    while q:
        cur = q.popleft()
        ans.append(cur)
        for u in adj[cur]:
            if not visited[u]:
                visited[u] = True
                q.append(u)
    return ans