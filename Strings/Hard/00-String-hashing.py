'''
You are given two strings ‘text’ and ’pat’, containing only lowercase alphabets.
Find the first index of ‘text’ where ‘pat’ matches with a substring of ‘text’, starting at that index.
Return -1 if such an index doesn’t exist.

https://www.codingninjas.com/studio/problems/first-occurence-of-a-pattern-in-a-text_8416393
'''
# Read Theory
# https://www.geeksforgeeks.org/string-hashing-using-polynomial-rolling-hash-function/
# https://cp-algorithms.com/string/string-hashing.html

# Trick is to hash every substring of 'text' of length 'pat'

def firstOccurence(text:str, pat: str) -> int:
    n = len(text)
    m = len(pat)
    if m > n:
        return -1
    h = {}
    for i in range(m-1, n):
        if text[i-m+1: i+1] not in h:
            h[text[i-m+1: i+1]] = i-m+1
    return h[pat] if pat in h else -1