- for point update, seg tree has TC = O(logN), but for range update we have to use lazy update to achieve that.
- make a lazy arr to store lazy values.
- during partial overlap, propagate lazy values to children during recursive call.
- during complete overlap, just add the lazy value and return from there.
- range update TC = logN
- range query TC = logN

<details>
<summary>Code</summary>

``` cpp


#include <bits/stdc++.h>
using namespace std;

void debug(vector<int>& arr){
    for (auto &i: arr){
        cout<<i<<" ";
    }
    cout<<endl;
}

vector<int> tree;
vector<int> lazy;

int merge(int a, int b){
    return min(a,b);
}

void propagate(int start, int end, int idx){
    if (start == end) {
        lazy[idx] = 0;
        return;
    }
    lazy[2*idx+1] += lazy[idx];
    lazy[2*idx+2] += lazy[idx];
    lazy[idx] = 0;
}

void build(vector<int>& arr, int idx, int start, int end){
    // time complexity = O(N)
    if (start == end){
        tree[idx] = arr[start];
        return;
    }
    int mid = (start + end) >> 1;
    build(arr, 2*idx+1, start, mid);
    build(arr, 2*idx+2, mid+1, end);
    tree[idx] = merge(tree[2*idx+1], tree[2*idx+2]);
}

// start and end of arr. idx is of seg-tree, pos is of arr.
// point update at pos
// time complexity = logN
// we won't update in actual arr
void update(int start, int end, int idx, int l, int r, int value){
    if (lazy[idx] != 0){
        tree[idx] += lazy[idx];
        propagate(start, end, idx);
    }
    if (start >= l && end <= r){
        tree[idx] += value;
        lazy[idx] += value;
        propagate(start, end, idx);
        return;
    }
    
    if (start > r || end < l) return; 
    int mid = (start + end) >> 1;
    update(start, mid, 2*idx+1, l, r, value);
    update(mid+1, end, 2*idx+2, l, r, value);
    tree[idx] = merge(tree[2*idx+1], tree[2*idx+2]);
}


int query(int start, int end, int l, int r, int idx){
    // time complexity = logN
    if (lazy[idx] != 0){
        tree[idx] += lazy[idx];
        propagate(start, end, idx);
    }
    // l.....start........end......r
    if (l <= start && end <= r) return tree[idx];
    if (r < start || l > end) return INT_MAX;;
    int mid= (start + end) >> 1;
    int left = query(start, mid, l, r, 2*idx+1);
    int right = query(mid+1, end, l, r, 2*idx+2);
    return merge(left, right);
}

int main()
{
    int n;
    cin>>n;
    // 1+2+3+...n = 2*n-1
    // size will be 2n if arr size is in the power of 2
    tree.resize(4*n, -1);
    lazy.resize(4*n, 0);
    vector<int> arr(n);
    for (auto &i: arr){
        cin >> i;
    }
    build(arr,0,0,n-1);
    cout<<query(0,n-1,1,2,0)<<endl;
    cout<<"tree ";
    debug(tree);
    update(0, n-1, 0, 0, 2, 4);
    cout<<"tree ";
    debug(tree);
    cout<<"lazy ";
    debug(lazy);
    
    cout<<query(0,n-1,0,2,0)<<endl;

    return 0;
}



```

</details>
