class Solution:
    def Solve(self, n, piles, h):
        low = 1
        high = max(piles)
        ans = high
        def check(hour):
            count = 0
            for bananas in piles:
                count += (bananas//hour)
                if bananas%hour:
                    count += 1
            return count <= h
                
        while low <= high:
            m = (low + high)//2
            if check(m):
                ans = m
                high = m-1
            else:
                low = m+1
        return ans

''' Similar Problems '''

# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/submissions/
# https://www.geeksforgeeks.org/problems/smallest-divisor/1
# https://www.geeksforgeeks.org/problems/capacity-to-ship-packages-within-d-days/1