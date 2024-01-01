
# Detect cycle in directed graph

# NORMAL DFS AND VISITED CONCEPT WILL NOT WORK HERE
# TRICK IS A NODE MUST BE VISITED ON THE SAME PATH


class Solution:
    #Function to detect cycle in a directed graph.
    def isCyclic(self, n, adj):
        visited = [False] * n
        path_visited = [False] * n
        
        def dfs(u):
            visited[u] = True
            path_visited[u] = True
            
            for v in adj[u]:
                if not visited[v]:
                    if dfs(v):
                        return True
                elif path_visited[v]:
                    return True
            
            path_visited[u] = False
            return False
        
        for u in range(n):
            if not visited[u]:
                if dfs(u):
                    return True
        
        return False
