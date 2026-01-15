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

