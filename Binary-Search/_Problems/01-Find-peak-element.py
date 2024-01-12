
# problem - https://leetcode.com/problems/find-peak-element/description/

class Solution:
    def findPeakElement(self, nums):
        n = len(nums)
        i = 0
        j = n-1
        while i <= j:
            m = (i+j)//2
            if m-1 >=0 and nums[m-1] > nums[m]:
                j = m-1
            elif m+1 < n and nums[m+1] > nums[m]:
                i = m+1
            else:
                return m
            
        