
class Solution 
{
    constructor(){
        this.visited = [];
        this.stack = [];
    }
    //Function to return list containing vertices in Topological order.
    topoSort(n, adj)
    {
        const dfs = (u) => { // use arrow function to use this keyword
            this.visited[u] = true;
            for (let v of adj[u]){
                if (!this.visited[v]) dfs(v);
            }
            this.stack.push(u);
        }
        for (let i=0; i<n; i++){
            this.visited.push(false);
        }
        for (let i=0; i<n; i++){
            if (!this.visited[i]) dfs(i);
        }
        return this.stack.reverse();
    }
}

// KAHN'S algorithm

/*

from collections import deque
class Solution:
    def topoSort(self, n, adj):
        indegree = [0 for _ in range(n)]
        for i in range(n):
            for u in adj[i]:
                indegree[u] += 1
        q = deque()
        ans = []
        for i,d in enumerate(indegree):
            if not d:
                q.append(i)
        while q:
            u = q.popleft()
            ans.append(u)
            for v in adj[u]:
                indegree[v] -= 1
                if not indegree[v]:
                    q.append(v)
        return ans
*/
