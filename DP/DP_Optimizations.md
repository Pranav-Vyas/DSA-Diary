### Longest Increasing Subsequence in NlogN

<details>
<summary>Explanation</summary>

We will use the dynamic programming array  
$d[0 \dots n]$ . This time  
$d[l]$  doesn't correspond to the element  
$a[i]$  or to a prefix of the array.  
$d[l]$  will be the smallest element at which an increasing subsequence of length  
$l$  ends.

Initially we assume  
$d[0] = -\infty$  and for all other lengths  
$d[l] = \infty$ .

We will again gradually process the numbers, first  
$a[0]$ , then  
$a[1]$ , etc, and in each step maintain the array  
$d[]$  so that it is up to date.  


<img width="1164" height="482" alt="image" src="https://github.com/user-attachments/assets/3b970582-565f-42cf-a05b-f03af42261fb" />

  
``` cpp
int fun(vector<int>& nums){
    int n = nums.size();
    vector<int> res;
    for (int i=0; i<n; i++){
        if (!res.size() || res.back() < nums[i]){
            res.push_back(nums[i]);
            continue;
        }
        auto it = lower_bound(res.begin(), res.end(), nums[i]);
        *it = nums[i];
    }
    return res.size();
}
```

</details>

<details>
<summary>Problems</summary>
  
- [https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/](https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/)

</details>



