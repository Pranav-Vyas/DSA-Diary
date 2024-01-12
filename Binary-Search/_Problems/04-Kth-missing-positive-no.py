
# https://www.codingninjas.com/studio/problems/kth-missing-element_893215

def missingK(vec, n, k):
    i = 0
    j = n-1
    while i <= j:
        m = (i+j)//2
        if (vec[m] - (m+1)) >= k:
            j = m-1
        else:
            i = m+1
    return j + 1 + k