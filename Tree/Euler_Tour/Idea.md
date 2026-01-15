- tree flatenning technique
- flatten the tree in the order of dfs

### Type 1
- consider below tree

<img width="720" height="535" alt="image" src="https://github.com/user-attachments/assets/007e548c-c569-417f-b5dc-19485d48ec8f" />


DFS - 1 2 1 3 5 3 6 3 1 4 1
#### Finding LCA
- LCA(5,6) = ?
- find the level of each node and store them in array.
- to find LCA of 5 & 6, we use segment tree to find minimum level of the range (5, 6).
- the node at min level will be LCA (3 in this case).
- TC (for q queries) - O(N) for dfs and O(Q * logN) => O(Q.logN)
- logN for segment tree query

<details>
<summary>Sample Code</summary>

``` cpp
vector<int> flat;
map<int,int> mp;
int idx = 0;

void dfs(int node, int par){
    if (mp.find(node) == mp.end()){
        mp[node] = idx;
    }
    flat.push_back(node);
    idx++;
    for (auto it: adj[node]){
        if (it == par) continue;
        dfs(it, node);
        idx++;
        flat.push_back(node);
    }
}

// call dfs to get flat array
// then using bfs, find level array 
// then apply range query for each LCA
```
  
</details>

### Type 2
- during dfs, we push the node, then traverse the subtree rooted at the node and then again push the node.
- helpful in the questions envolving subtree queries.
- TC - O(N)

<img width="681" height="553" alt="image" src="https://github.com/user-attachments/assets/0c29720d-4d7b-4017-84dd-2e71bda5b6ec" />


<details>
<summary>Sample Code</summary>

``` cpp
vector<int> flat;
map<int,pair<int,int>> mp;
int idx = 0;

void dfs(int node, int par){
    flat.push_back(node);
    mp[node].first = idx;
    idx++;
    for (auto it: adj[node]){
        if (it == par) continue;
        dfs(it, node);
    }
    mp[node].second = idx;
    flat.push_back(node);
    idx++;
}
```
  
</details>


