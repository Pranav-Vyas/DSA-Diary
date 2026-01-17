
### Rerooting DP

- Rerooting means we calculate the result by making each node the root of the tree.
- one DP array is responsible for calculating results within the subtree rooted at $i$. The other DP array calculates results outside of the subtree rooted at $i$.

#### Q. Tree Distances I - [https://cses.fi/problemset/task/1132](https://cses.fi/problemset/task/1132)

<details>
<summary>Idea</summary>

- The focus problem asks us to find for each node the maximum distance to another node. We can divide the problem into two parts.
- Define $f[x]$ as the maximum distance from node $x$ to any node in the subtree rooted at $x$, and $g[x]$ as the maximum distance from node $x$ to any node outside of the subtree rooted at $x$. Then the answer for node $x$ is $\max(f[x],g[x])$.
- $f[x]$ can be calculated using a DFS since $f[x]=\max(f[c])+1$, where $c$ is a child of $x$.
- $g[x]$ can also be calculated using a DFS as $g[c]=\max(g[x]+1, f[d]+2)$, where $c$ and $d$ are both children of $x$ with $c \neq d$.

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
    
</details>


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




___ 

#### Q. Tree Distances II - [https://cses.fi/problemset/task/1133](https://cses.fi/problemset/task/1133)

- approach is similar to above problem
- dfs() computes:
    - subtree[node] → subtree size
    - in[node] → sum of distances from node to nodes in its subtree
- dfs2() reroots DP using:
    ```  dp[child] = dp[parent] + n - 2 * subtree[child] ```
- Final dp[i] gives sum of distances from node i to all other nodes

<details>
<summary>Code</summary>

``` cpp

#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const int MAXN = 200005;

ll dp[MAXN];        // sum of distances from node to all others
ll subtree[MAXN];   // size of subtree
ll in[MAXN];        // sum of distances within subtree
ll n;

vector<ll> adj[MAXN];

void dfs(ll node, ll parent) {
    subtree[node] = 1;
    in[node] = 0;

    for (auto child : adj[node]) {
        if (child == parent) continue;

        dfs(child, node);

        subtree[node] += subtree[child];
        in[node] += in[child] + subtree[child];
    }
}

void dfs2(ll node, ll parent) {
    for (auto child : adj[node]) {
        if (child == parent) continue;

        dp[child] = dp[node] + n - 2 * subtree[child];
        dfs2(child, node);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;

    for (ll i = 0; i < n - 1; i++) {
        ll u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, 0);
    dp[1] = in[1];
    dfs2(1, 0);

    for (ll i = 1; i <= n; i++) {
        cout << dp[i] << " ";
    }

    return 0;
}


```
    
</details>

___

### Other Questions On DP
#### Q. Tree Matching - [https://cses.fi/problemset/task/1130](https://cses.fi/problemset/task/1130)

A matching is a set of edges where each node is an endpoint of at most one edge. What is the maximum number of edges in a matching?

<details>

<summary>Code</summary>

``` cpp

#include <bits/stdc++.h>
using namespace std;
 
int main()
{
    int n;
    cin>>n;
    vector<vector<int>> adj(n, vector<int>());
    for (int i=0; i<n-1; i++){
        int u,v;
        cin>>u>>v;
        adj[u-1].push_back(v-1);
        adj[v-1].push_back(u-1);
    }
    vector<vector<int>> dp(n, {-1,-1});
    function<int(int, int, int)> dfs = [&](int u, int par, int taken){
        if (dp[u][taken] != -1){
            return dp[u][taken];
        }
        // first take all the children without taking that edge
        int res = 0;
        for (int v: adj[u]){
            if (v == par) continue;
            res += dfs(v, u, 0);
        }
        // now only one edge can be added. If we take two children edges, it will be wrong
        int temp = res;
        if (taken == 0){
            for (int v: adj[u]){
                if (v == par) continue;
                int cur = temp + dfs(v, u, 1) + 1 - dp[v][0];
                res = max(res, cur);
            }
        }
        return dp[u][taken] = res;
        
    };
    cout<< dfs(0, -1, 0)<<endl;
 
    return 0;
}

```

</details>

___

#### Q. Three Paths on a Tree - [https://codeforces.com/problemset/problem/1294/F](https://codeforces.com/problemset/problem/1294/F)

Given a tree. Your task is to choose three distinct vertices a,b,c on this tree such that the number of edges which belong to at least one of the simple paths between a and b, b and c, or a and c is the maximum possible. See the notes section for a better understanding. The simple path is the path that visits each vertex at most once.

<details>

<summary>Idea</summary>
Find some diameter of the tree. Let a and b be the endpoints of this diameter (and first two vertices of the answer). You can prove yourself why it is always good to take the diameter and why any diameter can be taken in the answer. Then there are two cases: the length of the diameter is n−1 or the length of the diameter is less than n−1. In the first case, you can take any other vertex as the third vertex of the answer c, it will not affect the answer anyway. Otherwise, we can run multi-source bfs from all vertices of the diameter and take the farthest vertex as the third vertex of the answer. It is always true because we can take any diameter and the farthest vertex will increase the answer as much as possible.

- To find the diameter, first take any vertex(x) and find a vertex(a) which is at largest distance from x. 
- 'a' will be one end of diameter. Then find other vertex 'b' which is at largest dist from 'a'.
- a and b will be two end of diameter.
</details>

<details>

<summary>Code</summary>

``` cpp

#include <bits/stdc++.h>

using namespace std;

#define x first
#define y second

vector<int> p;
vector<vector<int>> g;

pair<int, int> dfs(int v, int par = -1, int dist = 0) {
	p[v] = par;
	pair<int, int> res = make_pair(dist, v);
	for (auto to : g[v]) {
		if (to == par) continue;
		res = max(res, dfs(to, v, dist + 1));
	}
	return res;
}

int main() {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
#endif
	
	int n;
	cin >> n;
	p = vector<int>(n);
	g = vector<vector<int>>(n);
	for (int i = 0; i < n - 1; ++i) {
		int x, y;
		cin >> x >> y;
		--x, --y;
		g[x].push_back(y);
		g[y].push_back(x);	
	}
	
	
	pair<int, int> da = dfs(0);
	pair<int, int> db = dfs(da.y);
	vector<int> diam;
	int v = db.y;
	while (v != da.y) {
		diam.push_back(v);
		v = p[v];
	}
	diam.push_back(da.y);
	
	if (int(diam.size()) == n) {
		cout << n - 1 << " " << endl << diam[0] + 1 << " " << diam[1] + 1 << " " << diam.back() + 1 << endl;
	} else {
		queue<int> q;
		vector<int> d(n, -1);
		for (auto v : diam) {
			d[v] = 0;
			q.push(v);
		}
		while (!q.empty()) {
			int v = q.front();
			q.pop();
			for (auto to : g[v]) {
				if (d[to] == -1) {
					d[to] = d[v] + 1;
					q.push(to);
				}
			}
		}
		pair<int, int> mx = make_pair(d[0], 0);
		for (int v = 1; v < n; ++v) {
			mx = max(mx, make_pair(d[v], v));
		}
		cout << int(diam.size()) - 1 + mx.x << endl << diam[0] + 1 << " " << mx.y + 1 << " " << diam.back() + 1 << endl;
	}
	
	return 0;
}

```

</details>












