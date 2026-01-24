# Linear Basis (XOR Basis) Algorithm - Step-by-Step Visualization
[https://codeforces.com/blog/entry/68953](https://codeforces.com/blog/entry/68953)  
  
This document visualizes the **Linear Basis** construction using the standard Gaussian Elimination approach (processing bits from MSB to LSB). To know more about it, refer the above blog.

## The Algorithm

The goal is to maintain a minimal set of numbers (basis) that can form any number in the original set via XOR operations.

**Key Property of this Implementation:**
Because we iterate from `d-1` down to `0`, `basis[i]` guarantees that the **Highest Set Bit (MSB)** of that stored vector is at position `i`.

```cpp
const int d = 5; // Dimension (5-bit numbers)
int basis[d];    // Stores the basis masks
int sz = 0;      // Current size of basis

void insertVector(int mask) {
    // Iterate from Most Significant Bit to Least Significant Bit
    for (int i = d - 1; i >= 0; i--) {
        // If the i-th bit is NOT set, this position is irrelevant for this number
        if ((mask & (1 << i)) == 0) continue; 

        // If no basis vector exists with MSB at position i
        if (!basis[i]) { 
            basis[i] = mask;
            ++sz;
            return; // Successful insertion
        }

        // XOR Reduction: Eliminate the i-th bit to keep searching lower bits
        mask ^= basis[i]; 
    }
}

```

### Dry Run

The Setup
- Dimension (d): 5 (We are working with 5-bit integers).
- Initial Basis: basis[5] = {0, 0, 0, 0, 0}
- Input Vectors to Insert:
  1. $23$ (1 0 1 1 1)
  2. $11$ (0 1 0 1 1)
  3. $10$ (0 1 0 1 0)

#### Step 1: Insert Vector $23$ (1 0 1 1 1)

i = 4:
- Check bit: Is the 4th bit of mask ($10111_2$) set? Yes.
- Check basis: Is basis[4] empty? Yes (it is 0).
- Action: Insert current mask into basis[4].
- basis[4] = 10111 ($23$).
- Return.  

Current Basis State:
- basis[4]: 10111 (23)
- Others: 0

#### Step 2: Insert Vector $11$ (0 1 0 1 1)
We call insertVector(01011). The loop runs from i = 4 down to 0.
1. i = 4:
   - Check bit: Is the 4th bit of mask ($01011_2$) set? No.
   - Action: Continue.
2. i = 3:
   - Check bit: Is the 3rd bit of mask set? Yes.
   - Check basis: Is basis[3] empty? Yes.
   - Action: Insert mask into basis[3].
   - basis[3] = 01011 ($11$).
   - Return.
     
Current Basis State:
- basis[4]: 10111 (23)
- basis[3]: 01011 (11)
- Others: 0

#### Step 3: Insert Vector $10$ (0 1 0 1 0)
This is the critical step where XOR reduction happens. We call insertVector(01010).
1. i = 4:
   - Check bit: Is 4th bit of mask set? No.
   - Action: Continue.
2. i = 3:Check bit: Is 3rd bit of mask set? Yes.
   - Check basis: Is basis[3] empty? No (it holds $11$).
   - Action: We must eliminate this bit to keep the basis independent.
   - mask = mask ^ basis[3]
   - mask = 01010 ^ 01011
   - mask = 00001 (New mask is $1$).
   - Note: Notice how the MSB (bit 3) became 0. We effectively "reduced" the vector.
3. i = 2:
   - Check bit: Is 2nd bit of mask ($00001_2$) set? No.
   - Action: Continue.
4. i = 1:
   - Check bit: Is 1st bit of mask ($00001_2$) set? No.
   - Action: Continue.
5. i = 0:
   - Check bit: Is 0th bit of mask ($00001_2$) set? Yes.
   - Check basis: Is basis[0] empty? Yes.
   - Action: Insert mask into basis[0].
   - basis[0] = 00001 ($1$).
   - Return.

#### After inserting $\{23, 11, 10\}$, our Linear Basis is:

|Index i |Basis Value (Binary)|Basis Value (Decimal)|Meaning                                |
|--------|--------------------|---------------------|---------------------------------------|
|basis[4]|1 0 1 1 1           |23                   |Controls the 4th bit (24)              |
|basis[3]|0 1 0 1 1           |11                   |Controls the 3rd bit (23)              |
|basis[2]|0 0 0 0 0           |0                    |No independent vector with MSB at bit 2|
|basis[1]|0 0 0 0 0           |0                    |No independent vector with MSB at bit 1|
|basis[0]|0 0 0 0 1           |1                    |Controls the 0th bit (20)              |


