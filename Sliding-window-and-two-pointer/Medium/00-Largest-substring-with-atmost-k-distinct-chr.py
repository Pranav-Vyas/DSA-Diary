
'''
You are given a string 'str' and an integer ‘K’. 
Your task is to find the length of the largest substring with at most ‘K’ distinct characters.

For example:
You are given ‘str’ = ‘abbbbbbc’ and ‘K’ = 2, then the substrings that can be formed are [‘abbbbbb’, ‘bbbbbbc’].
Hence the answer is 7.
'''

# Important - question is to find the length of largest substring, and not the no of substrings

from collections import defaultdict
def kDistinctChars(k, str):
    s = set()
    start = 0
    freq = defaultdict(int)
    res = 0
    for end in range(len(str)):
        freq[str[end]] += 1
        if freq[str[end]] == 1:
            s.add(str[end])
        if len(s) <= k:
            res = max(res, end-start+1)
        else:
            while start <= end and len(s) > k:
                freq[str[start]] -= 1
                if freq[str[start]] == 0:
                    s.remove(str[start])
                start += 1
            res = max(res, end-start+1)
    return res

# If asked to find no of substring
# do res += end-start+1 in place of res = max(res, end-start+1)
