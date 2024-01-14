'''
Given two sorted arrays array1 and array2 of size m and n respectively. 
Find the median of the two sorted arrays.
'''

'''
Input:
m = 3, n = 4
array1[] = {1,5,9}
array2[] = {2,3,6,7}
Output: 5
Explanation: The middle element for
{1,2,3,5,6,7,9} is 5
'''

class Solution:
    def MedianOfArrays(self, arr1, arr2):
        n1 = len(arr1)
        n2 = len(arr2)
        if n1 > n2:
            return self.MedianOfArrays(arr2, arr1)
        low = 0
        high = n1
        left = (n1+n2+1)//2
        while low <= high:
            mid1 = (low+high)//2
            mid2 = left - mid1
            l1, l2 = -float("inf"), -float("inf")
            r1, r2 = float("inf"), float("inf")
            if (mid1 < n1):
                r1 = arr1[mid1]
            if (mid2 < n2):
                r2 = arr2[mid2]
            if (mid1-1 >= 0):
                l1 = arr1[mid1-1]
            if (mid2-1 >= 0):
                l2 = arr2[mid2-1]
            if (l1 <= r2 and l2 <= r1):
                if (n1 + n2)%2 == 1:
                    return max(l1, l2)
                else:
                    sumi = max(l1,l2) + min(r1,r2)
                    if sumi%2:
                        return sumi/2
                    return sumi//2
            elif (l1 > r2):
                high = mid1-1
            else:
                low = mid1+1
        return 0