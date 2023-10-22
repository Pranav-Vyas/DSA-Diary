
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
