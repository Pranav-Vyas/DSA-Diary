
'''
You have been given a non-empty grid ‘mat’ with 'n' rows and 'm' columns consisting of only 0s and 1s. 
All the rows are sorted in ascending order.
Your task is to find the index of the row with the maximum number of ones.

Note: If two rows have the same number of ones, consider the one with a smaller index. 
If there's no row with at least 1 zero, return -1.
'''

def rowMaxOnes(mat, n, m):
    def lower_bound(i):
        low = 0
        high = m-1
        ans = n
        while low <= high:
            mid = (low+high)//2
            if mat[i][mid] == 1:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return n-ans
    idx, count = 0, 0
    for i in range(n):
        c = lower_bound(i)
        if c > count:
            idx = i
            count = c
    return idx if count else -1