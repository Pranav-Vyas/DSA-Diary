
# Detect cycle in undirected graph
# https://www.codingninjas.com/studio/problems/detect-cycle-in-an-undirected-graph-_758967

''' Using BFS '''

from collections import *

def detect(graph,n):
	q = deque()
	visited = [False for i in range(n)]
	def bfs(u):
		q.append((None,u))
		visited[u] = True
		while q:
			parent,u = q.popleft()
			for v in graph[u]:
				if not visited[v]:
					visited[v] = True
					q.append((u,v))
				elif v != parent:
					return True
		return False
	for u in range(n):
		if not visited[u]:
			flag = bfs(u)
			if flag:
				return True
	return False

V,E = map(int,input().split())
graph = [[] for _ in range(V)]
for _ in range(E):
	u,v = map(int,input().split())
	graph[u].append(v)
	graph[v].append(u)
print(detect(graph,V))

''' Using DFS '''

'''
class Solution {
  isCycleUtil(u, par, adj, vis) {
      vis[u] = true;
      for (let j = 0; j < adj[u].length; j++) {
          let v = adj[u][j];
          if (v == par) continue; // this line is important, do not put ===
          if (vis[v]) return true;
          if (this.isCycleUtil(v, u, adj, vis)) return true;
      }
      return false;
  }

  isCycle(V, adj) {
      let vis = new Array(V);
      vis.fill(false);
      for (let i = 0; i < V; i++) {
          if (!vis[i]) {
              let f = this.isCycleUtil(i, -1, adj, vis);
              if (f) return true;
          }
      }
      return false;
  }
}
'''