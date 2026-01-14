
Suppose we have a tree. 'N' node, 'Q' queries, 'k'. In each query, We want to find the Kth parent a node.  
- N < 1e5
- Q < 1e5
- k < N
### Normal approach
- Do a DFS on tree and maintain a parent array to store parent of each node.
- Then for each query, run w loop k times to find kth parent.
- Time Complexity - dfs O(n) + Q queries O(n * n). It will give TLE.

### Binary Lifting
- log2(1e5) = 17
- for each node, maintain a parent array of size 17.
- at each position i of 17, store the 2**ith parent.
- example - parent(17) will look like - 1st par, 2nd par, 4th par, 8th par, 16th par, 32th par and so on...
- if we want to find 11th parent (k = 11), binary of 11 = 1011. In 4 steps, we will find the 11th parent.
- parent array will be dp[node][17].
- Also, suppose node3 is node2's (x-1)th par, and node2 is node1's (x-1)th par. then node1's xth par will be node3.
- dp[node][x] = dp[dp[node][x-1]][x-1]
- TC - O(N.logN)

#### Sample code
``` cpp
void dfs(int node, int par, vector<int> adj[], vector<vector<int>>& dp){
    dp[node][0] = par;
    for (int i=1; i<=16; i++){
        dp[node][i] = dp[dp[node][i-1]][i-1];
    }
    for (auto it: adj[node]){
        if (it == par) continue;
        dfs(it, node, adj, dp);
    }
}

int main()
{
    int n;
    // tree in the form of adjacency list
    vector<int> adj[n+1];
    vector<vector<int>> dp(n+1, vector<int>(17,0));
    // call function to fill dp 
    dfs(1, 0, adj, dp);
    
    int q; // q queries
    while (q--){
        int node, k;
        cin>>node>>k;
        for (int i=16; i>=0; i--){
            if ((k >> i) & 1){
                node = dp[node][i];
            }
        }
        cout<<node<<endl;
    }
}
```

### LCA using binary lifting

<details>
<summary>
  Intuition
</summary>
  
- two nodes - a and b. find their levels. bring them on same level by getting the diff of levels and lifting lower level node by diff steps.
- start from most significant bit(MSB) - 16 to 0 and find 2^16th parent of both nodes.
- if pars are same - don't do anything, just go down further.
- if diff - lift the nodes to their respective parents
- if 0th parents are same - that's the LCA

<img width="1379" height="758" alt="image" src="https://github.com/user-attachments/assets/9ac044ae-107a-41e6-85f0-527c4b1eefb1" />

</details>

<details>
<summary> Sample code </summary>
  
``` cpp
    int main()
    {
        int n;
        // tree in the form of adjacency list
        vector<int> adj[n+1];
        vector<vector<int>> dp(n+1, vector<int>(17,0));
        // call function to fill dp 
        dfs(1, 0, adj, dp);
        
        // level array to store the level of each node
        vector<int> level(n+1,0);
        
        int q; // q queries
        while (q--){
            int a,b;
            cin>>a>>b;
            if (level[a] > level[b]){
                swap(a,b);
            }
            int diff = level[b] - level[a];
            // bring a and b on same level
            b = getKpar(b, diff);
            for (int i=16; i>=0; i++){
                if (dp[a][i] != dp[b][i]){
                    a = dp[a][i];
                    b = dp[b][i]; // if respective parents are unequal, lift the nodes up
                }
            }
            // print LCA
            cout<<dp[a][0]<<endl;
        }
    }
```
</details>

