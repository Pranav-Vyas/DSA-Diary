
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




