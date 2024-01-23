'''
https://leetcode.com/problems/subarrays-with-k-different-integers/description/

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
'''

# Question is based on no of substring having at most k distinct chrs

# Trick ans = atMostK(k, arr) - atMostK(k-1, arr)
# atMostK() is function to find no of substrings having at most k distinct chrs

from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums, k):
        def atMostK(k, nums):
            s = set()
            start = 0
            freq = defaultdict(int)
            res = 0
            for end in range(len(nums)):
                freq[nums[end]] += 1
                if freq[nums[end]] == 1:
                    s.add(nums[end])
                if len(s) <= k:
                    res += end-start+1
                else:
                    while start <= end and len(s) > k:
                        freq[nums[start]] -= 1
                        if freq[nums[start]] == 0:
                            s.remove(nums[start])
                        start += 1
                    res += end-start+1
            return res
        return atMostK(k,nums) - atMostK(k-1,nums)