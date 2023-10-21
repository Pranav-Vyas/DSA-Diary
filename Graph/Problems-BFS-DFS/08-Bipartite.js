/**
Linear graph with no cycle is always bipartite
Graph with even no cycle can be bipartite
Graph with odd cycle is not bipartite
*/

/**
 * @param {number[][]} graph
 * @return {boolean}
 */
var isBipartite = function(graph) {
    const n = graph.length
    const color = Array.from({length: n}, () => -1);
    function bfs(u){
        const q = new Dequeue();
        q.push(u);
        color[u] = 1;
        while (q.size){
            let v = q.front();
            q.popleft()
            for (let x of graph[v]) {
                if (color[x] !== -1) {
                    if (color[x] === color[v]) {
                        return false;
                    }
                } else {
                    color[x] = 1 - color[v];
                    q.push(x);
                }
            }
        }
        return true;
    }
    for (let u = 0; u<n; u++){
        if (color[u] === -1){
            if (!bfs(u)){
                return false;
            }
        }
    }
    return true;
};

// DFS solution - Python

/*
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [False for i in range(n)]
        h = {}
        def dfs(u,color):
            visited[u] = True
            h[u] = color
            for v in graph[u]:
                if not visited[v]:
                    if not dfs(v,1-color):
                        return False
                elif h[v] == color:
                    return False
            return True
        for i in range(n):
            if not visited[i]:
                if not dfs(i,1):
                    return False
        return True
*/

