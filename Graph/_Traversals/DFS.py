def dfsOfGraph(n, adj):
  ans = []
  visited = [False for i in range(n)]
  def dfs(v):
    visited[v] = True
    ans.append(v)
    for u in adj[v]:
      if not visited[u]:
        visited[u] = True
        dfs(u)
  for u in range(n):
    if not visited[u]:
      visited[u] = True
      dfs(u)
  return ans