### Rerooting dp

- Rerooting means we calculate the result by making each node the root of the tree.
- one DP array is responsible for calculating results within the subtree rooted at $i$. The other DP array calculates results outside of the subtree rooted at $i$.

##### Problem - [https://cses.fi/problemset/task/1132](https://cses.fi/problemset/task/1132)

- The focus problem asks us to find for each node the maximum distance to another node. We can divide the problem into two parts.
- Define $f[x]$ as the maximum distance from node $x$ to any node in the subtree rooted at $x$, and $g[x]$ as the maximum distance from node $x$ to any node outside of the subtree rooted at $x$. Then the answer for node $x$ is $\max(f[x],g[x])$.
- $f[x]$ can be calculated using a DFS since $f[x]=\max(f[c])+1$, where $c$ is a child of $x$.
- $g[x]$ can also be calculated using a DFS as $g[c]=\max(g[x]+1, f[d]+2)$, where $c$ and $d$ are both children of $x$ with $c \neq d$.

<details>
<summary>Sample code</summary>

```

in[node]   // longest downward path inside subtree of node
out[node]  // longest path going outside subtree of node

procedure DFS1(node, parent):
    in[node] ← 0

    for each child in adj[node]:
        if child = parent:
            continue

        DFS1(child, node)
        in[node] ← max(in[node], 1 + in[child])

procedure DFS2(node, parent):
    mx1 ← -1        // largest (1 + in[child])
    mx2 ← -1        // second largest
    heavyChild ← -1

    // find top two maximum values
    for each child in adj[node]:
        if child = parent:
            continue

        if in[child] + 1 > mx1:
            mx2 ← mx1
            mx1 ← in[child] + 1
            heavyChild ← child
        else if in[child] + 1 > mx2:
            mx2 ← in[child] + 1

    // propagate out[] to children
    for each child in adj[node]:
        if child = parent:
            continue

        longest ← mx1
        if child = heavyChild:
            longest ← mx2

        out[child] ← 1 + max(out[node], longest)
        DFS2(child, node)

procedure Solve():
    read n
    adj ← adjacency list of size n

    for i = 1 to n-1:
        read u, v
        add v to adj[u]
        add u to adj[v]

    out[1] ← 0
    DFS1(1, 0)
    DFS2(1, 0)

    for i = 1 to n:
        print max(in[i], out[i])

solve()

```
</details>

- in[node] → longest path going down

- out[node] → longest path going up or through parent
- mx1 (maximum path)
The largest value of 1 + in[child] among all children of the current node.
It represents the longest downward path starting from the current node through one of its children.

- mx2 (second maximum path)
The second largest value of 1 + in[child].
This is needed as a backup when the best path (mx1) comes from the same child we are currently propagating to.

- heavyChild
The child that produces mx1 (i.e., the child with the deepest subtree).
When computing out[child], we must not reuse the child’s own path, otherwise we would count the same path twice.

- Final answer per node = max(in[node], out[node])

- Overall complexity: O(N)

<img width="1505" height="781" alt="image" src="https://github.com/user-attachments/assets/78514e6c-f4ef-4a6e-b434-fe0a8f86cc44" />

