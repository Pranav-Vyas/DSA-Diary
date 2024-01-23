# https://leetcode.com/problems/repeated-string-match/description/

'''
Given two strings a and b, 
return the minimum number of times you should repeat string a so that string b is a substring of it. 
If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".

Input: a = "abcd", b = "cdabcdab"
Output: 3
'''


''' Method 1'''
# If len(a) < len(b), repeat 'a' until its len(a) > len(b). If after this point, b is not in a, then return -1

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        ans = 1
        temp = a
        while len(a) < len(b):
            a += temp
            ans += 1
        if b in a:
            return ans
        a += temp
        return ans+1 if b in a else -1
    
''' Method 2 - Rabin Carp algo '''
# https://leetcode.com/problems/repeated-string-match/solutions/416144/Rabin-Karp-algorithm-C++-implementation/