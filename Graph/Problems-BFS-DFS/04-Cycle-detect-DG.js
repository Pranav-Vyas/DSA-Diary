class Solution {
  isCycleUtil(u, par, adj, vis) {
      // marking the current vertex as visited.
      vis[u] = true;

      // iterating on all the adjacent vertices.
      for (let j = 0; j < adj[u].length; j++) {
          let v = adj[u][j];
          if (v == par) continue; // this line is important, do not put ===

          // if current vertex is visited, we return true else we
          // call the function recursively to detect the cycle.
          if (vis[v]) return true;
          if (this.isCycleUtil(v, u, adj, vis)) return true;
      }
      return false;
  }

  // Function to detect cycle in an undirected graph.
  isCycle(V, adj) {
      // using a boolean list to mark all the vertices as not visited.
      let vis = new Array(V);
      vis.fill(false);

      // iterating over all the vertices.
      for (let i = 0; i < V; i++) {
          // if vertex is not visited, we call the function to detect cycle.
          if (!vis[i]) {
              let f = this.isCycleUtil(i, -1, adj, vis);
              // if cycle is found, we return true.
              if (f) return true;
          }
      }
      return false;
  }
}