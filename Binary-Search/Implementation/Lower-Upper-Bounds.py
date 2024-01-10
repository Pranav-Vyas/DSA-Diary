''' Lower Bound '''

# find smallest index idx where arr[idx] >= target

def lowerBound(arr: [int], n: int, x: int) -> int:
    ans = n
    i,j = 0,n-1
    while i <= j:
        m = (i+j)//2
        if arr[m] >= x:
            ans = m
            j = m-1
        else:
            i = m+1
    return ans

''' Upper Bound '''

# The upper bound in a sorted array is the index of the first value that is greater than a given value. 

def upperBound(arr: [int], x: int, n: int) -> int:
    ans = n
    i = 0
    j = n-1
    while i<=j:
        m = (i+j)//2
        if arr[m] > x:
            j = m-1
            ans = m
        else:
            i = m+1
    return ans

# Applications
# - Search insert position
