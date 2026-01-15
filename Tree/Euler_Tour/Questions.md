### Question - [https://cses.fi/problemset/task/1137](https://cses.fi/problemset/task/1137)
Subtree queries

<details>
  <summary>Description</summary>
You are given a rooted tree consisting of n nodes. The nodes are numbered 1,2,...,n, and node 1 is the root. Each node has a value.
Your task is to process following types of queries:

change the value of node s to x
calculate the sum of values in the subtree of node s.
</details>

<details>
  <summary>Idea</summary>
  
- Use DFS Euler Tour to flatten the tree

- Each node appears twice (entry & exit)

- Store node value only at entry time

- Subtree sum = range sum between entry and exit

- Use Segment Tree for range sum & point update

<img width="1418" height="797" alt="image" src="https://github.com/user-attachments/assets/c58f567f-2a95-4c89-bfaa-2765bb0b2a5b" />

</details>

<details>
<summary>Solution</summary>
  
```
global timer = 0
flatTree = empty list

DFS(node, parent):
    in[node] = timer
    flatTree.push(node)
    timer++

    for each child in adj[node]:
        if child != parent:
            DFS(child, node)

    out[node] = timer
    flatTree.push(node)
    timer++

SegmentTree:
    tree[ ]      // size ≈ 4 * N

BUILD(node, start, end, arr):
    if start == end:
        tree[node] = arr[start]
        return

    mid = (start + end) / 2
    BUILD(2*node + 1, start, mid, arr)
    BUILD(2*node + 2, mid + 1, end, arr)

    tree[node] = tree[2*node + 1] + tree[2*node + 2]

QUERY(node, start, end, L, R):
    if R < start OR end < L:
        return 0

    if L <= start AND end <= R:
        return tree[node]

    mid = (start + end) / 2
    leftSum  = QUERY(2*node + 1, start, mid, L, R)
    rightSum = QUERY(2*node + 2, mid + 1, end, L, R)

    return leftSum + rightSum

UPDATE(node, start, end, index, value):
    if start == end:
        tree[node] = value
        return

    mid = (start + end) / 2
    if index <= mid:
        UPDATE(2*node + 1, start, mid, index, value)
    else:
        UPDATE(2*node + 2, mid + 1, end, index, value)

    tree[node] = tree[2*node + 1] + tree[2*node + 2]

MAIN:
    read n, q
    read values[1..n]
    read tree edges

    DFS(1, 0)
    BUILD(0, 0, 2*n - 1, segmentArray)

    while q queries:
        if type == 2:        // subtree sum
            read node
            QUERY(0, 0, 2*n - 1, in[node], out[node])
        else:               // update node value
            read node, val
           UPDATE(0, 0, 2*n - 1, in[node], val)

```
  
Time complexity

- Build: O(N)

- Query: O(log N)

- Update: O(log N)
  
</details>

___

### Question - [https://cses.fi/problemset/task/1138](https://cses.fi/problemset/task/1138)
Path queries

<details>
  <summary>Description</summary>
You are given a rooted tree consisting of n nodes. The nodes are numbered 1,2,\ldots,n, and node 1 is the root. Each node has a value.
Your task is to process following types of queries:

change the value of node s to x
calculate the sum of values on the path from the root to node s
</details>

<details>
  <summary>Idea</summary>
  
- idea is similar to previous ques. every node has two indices. put negative of node on second index.
- during query, nodes which are not in the required path will get cancelled.
- during update, put negative on second index
  
<img width="1390" height="770" alt="image" src="https://github.com/user-attachments/assets/b44e2beb-dbfb-424b-8e6c-e88e2b42143e" />

</details>

___

### Question - [https://codeforces.com/problemset/problem/1328/E](https://codeforces.com/problemset/problem/1328/E)
Tree Queries

<details>
  <summary>Description</summary>
You are given a rooted tree consisting of n nodes. In each query, you are given a set of nodes. You have to determine if there is a node u such that all the nodes of the given set are in the path from root(1) to node 2 or 1 distance away from any vertex in that path.

  <img width="1016" height="796" alt="image" src="https://github.com/user-attachments/assets/2d5d13f8-e789-40c6-8133-65182a2ccf76" />

</details>

<details>
  <summary>Idea</summary>

- the idea is type 1 euler tour (LCA)
- suppose query is 3 8 9 10
- find the node with largest level (10)
- if there is path, it will be from 10 to 1 (we don't have to find the shortest path)
- now one by one for each node in set, check its lca with 10
- if lca(n,10) = n, it will be in the path
- if not then, check the difference level(lca(n,10) - level(n) <= 1. if it is atmost 1, then it can be considered.
- otherwise not.
- **Can use binary lifting to find LCA.**

  
<img width="1541" height="806" alt="image" src="https://github.com/user-attachments/assets/204f4503-13eb-4718-9632-7c554dd37611" />


</details>
  
<details>
  <summary>
    Sample Code
  </summary>

```
Initialize dp[n+1][21] to 0
Initialize level[n+1] to 0

DFS(1, parent = 0)           // fills dp table and level array

while m > 0:
    m = m - 1

    read k
    read array A of size k

    maxLevel = -∞
    deepestNode = 0

    // find the deepest node in the query
    for each x in A:
        if level[x] > maxLevel:
            maxLevel = level[x]
            deepestNode = x

    valid = true

    // check condition using LCA
    for each x in A:
        ancestor = LCA(deepestNode, x)

        if |level[ancestor] - level[x]| > 1:
            valid = false
            break

    if valid:
        print "YES"
    else:
        print "NO"


```
  
</details>




