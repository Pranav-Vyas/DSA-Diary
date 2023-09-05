
'''
Given string num representing a non-negative integer num, and an integer k, 
return the smallest possible integer after removing k digits from num.
'''

'''
Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
'''

# time - O(n)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n=len(num)
        if k==1 and n==1:
            return '0'
        stack=[num[0]]
        for i in range(1,n):
            while stack and stack[-1]>num[i] and k:
                stack.pop()
                k-=1
            stack.append(num[i])
        while k and stack:
            stack.pop()
            k-=1
        return str(int(''.join(stack))) if stack else '0'
    
# JavaScript Sol

'''
var removeKdigits = function(num, k) {
    const s = [];
    for (let i = 0; i < num.length; i++){
        while (s.length && k && s[s.length-1] > num[i]){
            s.pop();
            k--;
        }
        s.push(num[i]);
    }
    
    while (k && s.length){
        s.pop();
        k--;
    }
    let j = 0;
    while (j < s.length && s[j] === '0'){
        j++;
    }
    return s.slice(j).join("") || "0";
};
'''
