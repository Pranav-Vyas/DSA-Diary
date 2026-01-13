- Used when N > 20.
- Loop through all subsets in the array and if the sum is equal to $x$, then increase our answer. Worst case this does about $2^{40}$ operations, which is too slow.
- We can divide the given array into two separate arrays. Let's say that the $\texttt{left}$ array runs from indexes $0$ to  $\frac{n}{2}-1$, and the  $\texttt{right}$ array runs from indexes $\frac{n}{2}$
 to $n-1$. Both arrays will have at most $20$ elements, so we can loop through all subsets of these two arrays in at most $2^{21}$ operations, which is perfectly fine.
- Time Complexity: $O(N\cdot 2^{N/2})$

### Question
[Partition Array Into Two Arrays to Minimize Sum Difference](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/description/)  
You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of length n to minimize the absolute difference of the sums of the arrays. To partition nums, put each element of nums into one of the two arrays.
Return the minimum possible absolute difference.  
<details>
  <summary>Examples</summary>

  ```
  Example 1:
  Input: nums = [3,9,7,3]
Output: 2
Explanation: One optimal partition is: [3,9] and [7,3].
The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.

Example 2:
Input: nums = [-36,36]
Output: 72
Explanation: One optimal partition is: [-36] and [36].
The absolute difference between the sums of the arrays is abs((-36) - (36)) = 72.
  ```
</details>
<details>
  <summary>Constraints</summary>
  
  ```
  1 <= n <= 15
  nums.length == 2 * n
  -107 <= nums[i] <= 107
  ```
</details>
<details>
  <summary>Solution</summary>
    
    ```cpp
    
    class Solution {
    public:
        int minimumDifference(vector<int>& nums) {
            int n = nums.size();
            int m = n/2;
            map<int,vector<int>> mp;
            for (int mask = 0; mask < (1<<m); mask++){
                int s = 0;
                for (int i = 0; i<m; i++){
                    if (mask & (1<<i)){
                        s += nums[i];
                    }
                }
                mp[__builtin_popcount(mask)].push_back(s);
            }
            int total = 0;
            for (int i = 0; i<m; i++){
                total += (nums[i] + nums[n-1-i]);
                sort(mp[i].begin(),mp[i].end());
            }
            int best = 1e9;
            for (int mask = 0; mask < (1<<m); mask++){
                int s = 0;
                for (int i = 0; i<m; i++){
                    if (mask & (1<<i)){
                        s += nums[m+i];
                    }
                }
                int c = __builtin_popcount(mask);
                int tar = total/2 - s;
                auto it = lower_bound(mp[m-c].begin(), mp[m-c].end(), tar);
                if(it != mp[m-c].end()){
                    best = min(best, abs(total - 2*(s + *it)));
                }
                if(it != mp[m-c].begin()){
                    it--;
                    best = min(best, abs(total - 2*(s + *it)));
                }
            }
            return best;
        }
    };
    ```
  
</details>


### Other
- [https://leetcode.com/problems/closest-subsequence-sum/](https://leetcode.com/problems/closest-subsequence-sum/)
- [https://leetcode.com/problems/split-array-with-same-average/description/](https://leetcode.com/problems/split-array-with-same-average/description/)
- [https://codeforces.com/contest/1006/problem/F](https://codeforces.com/contest/1006/problem/F)
- [https://codeforces.com/contest/888/problem/E](https://codeforces.com/contest/888/problem/E)
