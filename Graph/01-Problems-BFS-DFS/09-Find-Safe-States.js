
// https://leetcode.com/problems/find-eventual-safe-states/description/

var eventualSafeNodes = function(graph) {
  n = graph.length;
  const visited = Array.from({length: n}, () => false);
  const pathVisited = Array.from({length: n}, () => false);
  const safe = Array.from({length: n}, () => false);
  const ans = [];
  function dfs(u){
      visited[u] = true;
      pathVisited[u] = true;
      for (let v of graph[u]){
          if (!visited[v]){
              if (!dfs(v)) return false;
          } else if (pathVisited[v]){
              return false;
          }
      }
      pathVisited[u] = false;
      safe[u] = true;
      return true;
  }
  for (let u=0; u<n; u++){
      if (!visited[u]){
          dfs(u);
      }
  }
  safe.forEach((u,i) => {
      if (u){
          ans.push(i);
      }
  })
  return ans;
};

/************ Another solution - Topological Sort ******************* */

/*
from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = [[] for _ in range(n)]
        indeg = [0 for _ in range(n)]
        for u in range(n):
            for v in graph[u]:
                adj[v].append(u)
                indeg[u] += 1
        q = deque()
        topo = []
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
        return sorted(topo)
*/
