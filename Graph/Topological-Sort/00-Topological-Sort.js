
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
