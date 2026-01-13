
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
