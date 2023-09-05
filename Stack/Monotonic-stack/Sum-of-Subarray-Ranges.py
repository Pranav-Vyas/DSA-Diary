
'''
You are given an integer array nums.
The range of a subarray of nums is the difference between the largest and smallest element in the subarray.
Return the sum of all subarray ranges of nums.
'''

# Trick - use previous calc result to find max and min of new subarray

# DP implementation - O(n**2)

class Solution:
    def subArrayRanges(self, nums) -> int:   
      n = len(nums)
      ans = 0
      for i in range(n):
          mini = float('inf')
          maxi = -float('inf')
          for j in range(i,-1,-1):
              mini = min(mini,nums[j])
              maxi = max(maxi,nums[j])
              ans += (maxi-mini)
      return ans
    
# Stack Method 1 - O(n)

'''
- (max - min) + (max - min) + (max - min) == (max + max + max) - (min + min + min)
- first subtract min of all subarray from ans
- then add max of all subarray to ans or can be done in opposite order
- for every popped 'x', check in how many subarray can it be used as min
- do same for max
'''

class Solution:
    def subArrayRanges(self, nums) -> int:
        res = 0
        inf = float('inf')
        A = [-inf] + nums + [-inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res -= A[j] * (i - j) * (j - k)
            s.append(i)
            
        A = [inf] + nums + [inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] < x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res
    
# Stack Method 2 - O(n)

'''
- stack[i] = [i, currMax]
- currMax is not the maximum of all elements till 'i', it is the sum of maximum of all subarrays till 'i'
- for every next nums[j],
  - pop from stack if nums[j] >= stack[-1][0]
  - suppose popping stops at stack[i], it means nums[j] is max among all elements between i - j
  - so sum of max of all subarray from i to j = nums[j]*(j-stack[-1][0])
  - and we already know the ans of 0 - i stored in stack[-1][1]
'''
class Solution:
    def subArrayRanges(self, nums) -> int:
        n = len(nums)
        maxi = 0
        mini = 0
        stack = [(-1,0)]
        for i in range(n):
            curMax = 0
            while len(stack) > 1 and nums[stack[-1][0]] <= nums[i]:
                stack.pop()
            curMax = stack[-1][1] + nums[i]*(i-stack[-1][0])
            maxi += curMax
            stack.append((i,curMax))
        stack = [(-1,0)]
        for i in range(n):
            curMin = 0
            while len(stack) > 1 and nums[stack[-1][0]] >= nums[i]:
                stack.pop()
            curMin = stack[-1][1] + nums[i]*(i-stack[-1][0])
            mini += curMin
            stack.append((i,curMin))
        return maxi - mini
