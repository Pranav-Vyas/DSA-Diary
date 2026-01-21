## Basic
#### [Kth One](https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/B)

<details>
<summary>Code
</summary>

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
 
 
int query(vector<int>& arr, int start, int end, int k, int idx){
    // time complexity = logN
    // l.....start........end......r
    if (start == end) return start;
    int mid= (start + end) >> 1;
    int left = tree[2*idx+1];
    int right = tree[2*idx+2];
    if (left >= k){
        return query(arr, start, mid, k, 2*idx+1);
    } else {
        return query(arr, mid+1, end, k-left, 2*idx+2);
    }
}
 
int main()
{
    int n,m;
    cin>>n>>m;
    tree.resize(4*n, 0);
    vector<int> arr(n);
    for (auto &i: arr){
        cin >> i;
    }
    build(arr,0,0,n-1);
    while(m--){
        int op, x;
        cin>>op>>x;
        if (op == 1){
            update(arr, 0, n-1, 0, x, 1-arr[x]);
        } else {
            cout<<query(arr, 0, n-1, x+1, 0)<<endl;
        }
    }
 
    return 0;
}

```

</details>


#### [First element at least X - 2](https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/D)

<details>
<summary>Code
</summary>

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
    tree[idx] = max(tree[2*idx+1], tree[2*idx+2]);
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
    tree[idx] = max(tree[2*idx+1], tree[2*idx+2]);
}
 
 
int query(int idx, int start, int end, int x, int l) {
    // 1. If the current range is entirely below our search index or 
    // the max in this range is less than x, no valid index exists here.
    if (end < l || tree[idx] < x) {
        return -1;
    }
 
    // 2. Leaf node reached
    if (start == end) {
        return start;
    }
 
    int mid = (start + end) >> 1;
    
    // 3. Try left child first
    int res = query(2 * idx + 1, start, mid, x, l);
    
    // 4. If left child didn't have it, try right child
    if (res == -1) {
        res = query(2 * idx + 2, mid + 1, end, x, l);
    }
    
    return res;
}
 
int main()
{
    int n,m;
    cin>>n>>m;
    tree.resize(4*n, 0);
    vector<int> arr(n);
    for (auto &i: arr){
        cin >> i;
    }
    build(arr,0,0,n-1);
    while(m--){
        int op, x, y;
        cin>>op>>x>>y;
        if (op == 1){
            update(arr, 0, n-1, 0, x, y);
        } else {
            cout<<query(0, 0, n-1, x, y)<<endl;
        }
    }
 
    return 0;
}

```

</details>


#### [Segment with the Maximum Sum](https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/A)

<details>
<summary>Code
</summary>

``` cpp

#include <bits/stdc++.h>
using namespace std;
 
vector<vector<long long>> tree;

// tree[idx][0] -> sum of the whole subtree
// tree[idx][1] -> maximum sum of any segment (which will be ans finally)
// tree[idx][2] -> maximum sum of a segment starting from left most idx of that subtree
// tree[idx][3] -> maximum sum of a segment starting from right most idx of that subtree

void merge(int idx){
    int l = 2*idx+1;
    int r = 2*idx+2;
    tree[idx][0] = tree[l][0] + tree[r][0];
    tree[idx][1] = max<long long>({tree[l][1], tree[r][1], tree[l][3] + tree[r][2], 0});
    tree[idx][2] = max<long long>({tree[l][2], tree[l][0] + tree[r][2], 0});
    tree[idx][3] = max<long long>({tree[r][3], tree[r][0] + tree[l][3], 0});
}
 
void build(vector<int>& arr, int idx, int start, int end){
    // time complexity = O(N)
    if (start == end){
        tree[idx] = {1ll * arr[start], max(arr[start],0), max(arr[start],0), max(arr[start],0)};
        return;
    }
    int mid = (start + end) >> 1;
    build(arr, 2*idx+1, start, mid);
    build(arr, 2*idx+2, mid+1, end);
    merge(idx);
}
 
// start and end of arr. idx is of seg-tree, pos is of arr.
// point update at pos
// time complexity = logN
void update(vector<int>& arr, int start, int end, int idx, int pos, int value){
    // leaf
    if (start == end){
        arr[pos] = value;
        tree[idx] = {1ll *arr[start], max(arr[start],0), max(arr[start],0), max(arr[start],0)};
        return;
    }
    int mid = (start + end) >>1;
    if (pos <= mid){
        update(arr, start, mid, 2*idx+1, pos, value);
    } else {
        update(arr, mid+1, end, 2*idx+2, pos, value);
    }
    merge(idx);
}
 
int main()
{
    int n,m;
    cin>>n>>m;
    tree.resize(4*n, vector<long long>(4,0));
    vector<int> arr(n);
    for (auto &i: arr){
        cin >> i;
    }
    build(arr,0,0,n-1);
    cout<<tree[0][1]<<endl;
    while(m--){
        int i, x;
        cin>>i>>x;
        update(arr, 0, n-1, 0, i, x);
        cout<<tree[0][1]<<endl;
    }
 
    return 0;
}

```

</details>

