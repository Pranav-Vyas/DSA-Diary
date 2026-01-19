
There can be 3 types of problems:
#### Type 1:
- static array + range queries
- e.g. [1,5,3,2,4], for each query [l,r], return sum
- **Prefix sum**
- O(Q) + O(N)

#### Type 2:
- initial array + range update queries + final array queries
- e.g. [1,5,3,2,4], first all the range updates are there like for each (l,r) add x. Then return final array
- **Difference array**
- O(Q) + O(N)

#### Type 3:
- given an array and two operations
  1. (l,r) -> output sum of values from l to r. (range query) (logN)
  2. update arr[pos] = val (point update) (logN)
- **Segment tree**

### Segment tree

- if you are at a node and you need the answer of its complete range --> directly return its value.
- if you are at a node and none of its elements contribute to your answer --> return from there (don't go down).

  
#### Case 1: Complete overlap - don't go down
[...........]      - query range  
--[.......]        - node range  

#### Case 2: Partial overlap - go down
[...........]      - query range  
----[..........]   - node range  

#### Case 3: No overlap - don't go down
[....]             - query range  
-------[.......]   - node range  

<details>
<summary>Image</summary>

<img width="1062" height="681" alt="image" src="https://github.com/user-attachments/assets/fa136dcb-033d-4819-9977-112b49f2e4de" />
  
</details>

### Why it is O(logN) ?

<details>
<summary>Explaination</summary>

- because any any level we cannot visit more than 4 nodes.
- to visit maximum node, there should be maximum partial overlap
- suppose at level 1, we have partial overlap. we go down and both query range and node range are divided into two.
- at level 2, we cannot have more than 2 partial overlaps. because range is continuous.
- only terminal nodes will have partial overlap and hence divide. internal nodes will have complete overlap.
- so it is 4*logN = logN
  

<img width="1062" height="681" alt="image" src="https://github.com/user-attachments/assets/4a541908-7354-48ae-9a62-13e23b99a3b4" />


</details>

### Code

``` cpp

#include <bits/stdc++.h>
using namespace std;

vector<int> tree;

void build(vector<int>& arr, int idx, int start, int end){
    // time complexity = O(N)
    if (start == end){
        tree[idx] = arr[start];
        return;
    }
    int mid = (start + end) >> 1;
    build(arr, 2*idx+1, start, mid);
    build(arr, 2*idx+2, mid+1, end);
    tree[idx] = tree[2*idx+1] + tree[2*idx+2];
}

// start and end of arr. idx is of seg-tree, pos is of arr.
// point update at pos
// time complexity = logN
void update(vector<int>& arr, int start, int end, int idx, int pos, int value){
    // leaf
    if (start == end){
        arr[pos] = value;
        tree[idx] = value;
        return;
    }
    int mid = (start + end) >>1;
    if (mid >= pos){
        update(arr, start, mid, 2*idx+1, pos, value);
    } else {
        update(arr, mid+1, end, 2*idx+2, pos, value);
        
    }
    tree[idx] = tree[2*idx+1] + tree[2*idx+2];
}


int query(vector<int>& arr, int start, int end, int l, int r, int idx){
    // time complexity = logN
    // l.....start........end......r
    if (l <= start && end <= r) return tree[idx];
    if (r < start || l > end) return 0;
    int mid= (start + end) >> 1;
    int left = query(arr, start, mid, l, r, 2*idx+1);
    int right = query(arr, mid+1, end, l, r, 2*idx+2);
    return left+right;
}

int main()
{
    int n;
    cin>>n;
    // 1+2+3+...n = 2*n-1
    // size will be 2n if arr size is in the power of 2
    tree.resize(2*n, -1);
    vector<int> arr(n);
    for (auto &i: arr){
        cin >> i;
    }
    build(arr,0,0,n-1);
    cout<<query(arr,0,n-1,0,2,0)<<endl;
    
    update(arr, 0, n-1, 0, 2, 4);
    cout<<query(arr,0,n-1,0,2,0)<<endl;

    return 0;
}

```

#### Changes in the implementation based on question
- current implementation
- update value at pos -> value
- give a range sum
- arr[pos] = value
  
--------------------  
- update value at pos = current val + value
- give minimum of range
- arr[pos] += value
- in build -> take min
- in update -> arr[pos] += val and take min
- in query -> return infinity if no overlap  

--------------------  
- update value at pos = gcd(current val, value)
- give xor of range
- arr[pos] += value
- in build -> take xor
- in update -> arr[pos] = __gcd(arr[pos], val) and take xor
- in query -> return 0 if no overlap else xor of left and right

