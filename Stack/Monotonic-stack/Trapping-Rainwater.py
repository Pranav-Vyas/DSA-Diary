
'''

Problem Statement: Given an array of non-negative integers representation elevation of ground. 
Your task is to find the water that can be trapped after rain.

https://leetcode.com/problems/trapping-rain-water/description/

'''

# Solution

'''
- for each height h, find Next Greater Element(NGE) of right and store in arr1.
- for each height h, find Next Greater Element(NGE) of left and store in arr2.
- for each height h, calculate min(arr1[i], arr2[j]) - h and add it to answer
- return ans.
'''

# time - O(n)
# space = O(n)

class Solution:
  def trap(self, height) -> int:
    left = []
    maxi = 0
    for x in height:
        maxi = max(maxi,x)
        left.append(maxi)
    right = []
    maxi = 0
    for x in reversed(height):
        maxi = max(maxi,x)
        right.append(maxi)
    right.reverse()
    ans = 0
    for i in range(len(height)):
        ans += (min(left[i],right[i])-height[i])
    return ans
