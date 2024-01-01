
/**
 * mat is matrix of n*n
 * mat[i][u] means i is connected to u
 * it is undirected graph
 * find no of connected components
 * 
 * problem - https://leetcode.com/problems/number-of-provinces/description/
 * 
 * @param {*} mat 
 * @returns 
 */

var findCircleNum = function(mat) {
  let n = mat.length;
  let visited = Array.from({length: n}, () => false);
  let count = 0;
  function dfs(v, visited){
      visited[v] = true;
      for (let u = 0; u < n; u++){
          if (mat[v][u] === 1 && !visited[u]){
              visited[u] = true;
              dfs(u, visited);
          }
      }
  }
  for (let u = 0; u < n; u++){
      if (!visited[u]){
          visited[u] = true;
          count++;
          dfs(u, visited);
      }
  }
  return count;
};
