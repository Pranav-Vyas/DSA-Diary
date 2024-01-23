# https://www.codingninjas.com/studio/problems/minimum-window-subsequence_2181133

'''
You are given two strings ‘S’ and ‘T’. Your task is to find the minimum (Contiguous) substring ‘W’ of ‘S’, 
such that ‘T’ is a subsequence of ‘W’

input:
abcdebdde
bde

output:
bcde
'''

# Trick -------> use DP

def minWindow(s, t):
    m = len(s)
    n = len(t)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1,n+1):
        dp[i][0] = float('inf')
    for i in range(1,n+1):
        for j in range(1,m+1):
            if t[i-1] == s[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = dp[i][j-1]+1
    ans = ""
    size = float("inf")
    for j in range(1,m+1):
        if dp[n][j] < size:
            size = dp[n][j]
            ans = s[j-dp[n][j]: j]
    return ans
