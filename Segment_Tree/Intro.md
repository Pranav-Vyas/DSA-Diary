
There can be 3 types of problems:
#### Type 1:
- static array + range queries
- e.g. [1,5,3,2,4], for each query [l,r], return sum
- **Prefix sum**
- O(Q) + O(N)

##### Type 2:
- initial array + range update queries + final array queries
- e.g. [1,5,3,2,4], first all the range updates are there like for each (l,r) add x. Then return final array
- **Difference array**
- O(Q) + O(N)

##### Type 3:
- given an array and two operations
  1. (l,r) -> output sum of values from l to r. (range query) (logN)
  2. update arr[pos] = val (point update) (logN)
- **Segment tree**
