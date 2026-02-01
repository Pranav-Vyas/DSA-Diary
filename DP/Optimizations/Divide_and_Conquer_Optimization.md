Divide and Conquer DP Optimization is a technique used to reduce the time complexity of dynamic programming problems from $O(K \cdot N^2)$ to $O(K \cdot N \log N)$.It is specifically applicable to problems where you need to partition a sequence into $K$ groups (or layers) and the "optimal splitting point" behaves monotonically.  
Blog - [https://cp-algorithms.com/dynamic_programming/divide-and-conquer-dp.html](https://cp-algorithms.com/dynamic_programming/divide-and-conquer-dp.html)  

#### Standard Recurrence

This optimization applies to DP relations of the form: $$dp[k][i] = \min_{0 \le j < i} \{ dp[k-1][j] + Cost(j+1, i) \}$$
- Where: $dp[k][i]$ is the minimum cost to divide the first $i$ elements into $k$ groups.
- $Cost(j+1, i)$ is the cost of a single group containing elements from index $j+1$ to $i$.
- The Naive Approach: To compute $dp[k][i]$, you iterate through all possible split points $j < i$.
- Calculating one state takes $O(N)$.
- There are $K \times N$ states. Total Complexity: $O(K \cdot N^2)$.

#### The Optimization Condition

- You can apply Divide and Conquer optimization if the problem satisfies the Quadrangle Inequality, which implies the Monotonicity of Optimal Points.
- If the best place to split the array for the first $i$ elements is at index $x$, then for the first $i+1$ elements, the best split must be at index $x$ or to the right of $x$. It never moves to the left.
- Let $opt[k][i]$ be the index $j$ that minimizes the equation for $dp[k][i]$. The condition is:$$opt[k][i] \le opt[k][i+1]$$

#### Algorithm
 
- For a fixed layer $k$, we want to compute $dp[k][i]$ for a range of indices $i \in [L, R]$.
- We know the optimal split point $j$ must fall within some search range $[optL, optR]$.
- Compute Middle: Pick the middle index $mid = (L + R) / 2$.Find Best Split:
- Iterate through all possible $j$ between $optL$ and $\min(mid, optR)$ to find the $j$ that minimizes $dp[k][mid]$.
- Let's call this best split $best\_k$.
- Conquer Left: Recursively solve for the left half $[L, mid-1]$. Because of monotonicity, we know their optimal splits must be in range $[optL, best\_k]$.
- Conquer Right: Recursively solve for the right half $[mid+1, R]$. We know their optimal splits must be in range $[best\_k, optR]$.
- By restricting the search bounds ($optL, optR$) at each step, we ensure that every index $j$ is visited a constant number of times per layer level in the recursion tree.

#### Example Problem

Problem: [https://leetcode.com/problems/minimum-partition-score/description/](https://leetcode.com/problems/minimum-partition-score/description/)  
- Partition an array nums of size $N$ into $K$ subarrays to minimize the total score. Score Function: $\sum \frac{S \cdot (S+1)}{2}$, where $S$ is the sum of a subarray.

#### Naive Solution
- State: dp[k][i] = Minimum score to partition the first i elements (prefix nums[0...i-1]) into k groups.
- Transition: To calculate dp[k][i], we iterate through all possible split points j (where $j < i$): $$dp[k][i] = \min_{0 \le j < i} \{ dp[k-1][j] + Cost(j, i) \}$$ (Meaning: Take the optimal solution for $k-1$ groups ending at $j$, and add the cost of the new group from $j$ to $i$.)Complexity: $O(K \cdot N^2)$.

#### The Optimized Algo

- Instead of computing dp[k][1], then dp[k][2], etc., we compute the entire row k using a recursive function that behaves like Binary Search.  

**Function:** recur(k, L, R, optL, optR)
- k: The current number of groups we are building.
- L, R: The range of states (indices $1 \dots N$) we want to compute values for.
- optL, optR: The valid search range for the optimal split point $j$.

**Logic:**  
- Find Midpoint: We pick the middle index of our target range: m = (L + R) / 2.
- We will calculate the answer for dp[k][m] first.
- Find Best Split for Mid: We iterate $j$ from optL to min(m-1, optR) to find which split minimizes the cost for dp[k][m].
- We store the best value in dp[m][k].
- We store the index of the best split in bestCutPos.
- Divide and Conquer (The Optimization): Now that we know the best split for m is bestCutPos, we can restrict the search for the left and right halves:
- Left Half (L to m-1): Since these indices are smaller than m, their optimal split cannot be to the right of bestCutPos. $\rightarrow$ New Search Range: [optL, bestCutPos]
- Right Half (m+1 to R): Since these indices are larger than m, their optimal split cannot be to the left of bestCutPos. $\rightarrow$ New Search Range: [bestCutPos, optR]  

``` cpp

class Solution {
public:
    vector<long long> presum;
    vector<vector<long long>> dp;

    long long cost(int i, int j) {
        long long s = presum[j] - presum[i];
        return ((s + 1) * s) / 2;
    }

    void recur(int k, int l, int r, int optl, int optr){
        if (l > r) return;
        int m = (l+r) >> 1;
        int bestCutPos = -1;
        for (int j = optl; j <= min(m-1, optr); j++){
            if (dp[j][k-1] == -1) continue;
            long long val = dp[j][k-1] + cost(j, m);
            if (dp[m][k] == -1 || val < dp[m][k]){
                dp[m][k] = val;
                bestCutPos = j;
            }
        }
        if (bestCutPos == -1) {
            recur(k, m+1, r, optl, optr);
            return;
        }
        recur(k, l, m-1, optl, bestCutPos);
        recur(k, m+1, r, bestCutPos, optr);
    }

    long long minPartitionScore(vector<int>& nums, int k) {
        int n = nums.size();
        presum = vector<long long>(n+1, 0);
        for (int i=0; i<n; i++){
            presum[i+1] = presum[i]+nums[i];
        }
        dp = vector<vector<long long>>(n+1, vector<long long>(k+1, -1));
        dp[0][0] = 0;
        for (int grp = 1; grp <= k; grp++){
            recur(grp, 1, n, 0, n);
        }
        return dp[n][k];
    }
};

```

#### Cases where Quadrangle Inequality may follows

- Polynomial Costs on Non-Negative Arrays: Cost: $(Sum)^2$, $(Sum)^3$, or $(Sum)^k$
- Geometric / Distance Costs: Cost: $(i - j)^2$ or $(i - j)^p$.
- Product Costs (Time $\times$ Weight): Cost: $(Sum\_Weights) \times (Sum\_Time)$.

#### Cases Where It FAILS
- Negative Numbers (Non-Monotonic Prefix Sums)
- Modular Arithmetic: Cost: $(Sum) \% M$.
- Bitwise Operations
- Absolute Differences (Oscillating): Cost: $|A[i] - A[j]|$.


