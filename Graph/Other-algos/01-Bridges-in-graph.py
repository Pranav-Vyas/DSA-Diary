
# problem - https://leetcode.com/problems/critical-connections-in-a-network/description/

class Solution:
    def criticalConnections(self, n, connections):
        time = [0 for i in range(n)]
        low = [0 for i in range(n)]
        visited = [False for i in range(n)]
        graph = [[] for _ in range(n)]
        timer = [0]
        bridges = []
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(u,parent):
            visited[u] = True
            time[u] = timer[0]
            low[u] = timer[0]
            timer[0] += 1
            for v in graph[u]:
                if v == parent:
                    continue
                if not visited[v]:
                    dfs(v,u)
                    low[u] = min(low[u],low[v])
                    if low[v] > time[u]:
                        bridges.append([u,v])
                else:
                    low[u] = min(low[u],low[v])
        dfs(0,-1)
        return bridges