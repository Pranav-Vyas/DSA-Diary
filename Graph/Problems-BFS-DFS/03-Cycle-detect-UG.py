
# Detect cycle in undirected graph
# https://www.codingninjas.com/studio/problems/detect-cycle-in-an-undirected-graph-_758967

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