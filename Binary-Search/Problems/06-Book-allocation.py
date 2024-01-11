# https://www.codingninjas.com/studio/problems/allocate-books_1090540

def findPages(arr, n, m):
    if m > n:
        return -1
    def check(pages):
        prev = 0
        count = 1
        for p in arr:
            if prev + p <= pages:
                prev += p
            else:
                count += 1
                prev = p
        return count
    low = max(arr)
    high = sum(arr)
    while low <= high:
        mid = (low+high)//2
        if check(mid) > m:
            low = mid+1
        else:
            high = mid-1
    return low