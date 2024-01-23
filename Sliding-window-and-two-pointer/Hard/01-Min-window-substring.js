/**
 * https://leetcode.com/problems/minimum-window-substring/description/
 * 
 * Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. 
 If there is no such substring, return the empty string "".
 * 
 Example

 Input: s = "ADOBECODEBANC", t = "ABC"
 Output: "BANC"
 */

 var minWindow = function(s, t) {
  let count = {}
  let n = s.length;
  let m = t.length;
  if (m > n){
      return "";
  }
  for (let i = 0; i<m; i++){
      let c = t[i];
      if (count[c] !== undefined){
          count[c]++;
      } else {
          count[c] = 1;
      }
  }
  let freq = {};
  function check(){
      for (let c in count){
          if (freq[c] === undefined || freq[c] < count[c]){
              return false;
          }
      }
      return true;
  }
  let start = 0;
  let ans = "";
  let len = n+1;
  for (let end = 0; end < n; end++){
      let c = s[end];
      if (freq[c] === undefined){
          freq[c] = 1
      } else{
          freq[c]++;
      }
      while (start <= end && check()){
          if (end-start+1 < len){
              ans = s.slice(start,end+1);
              len = ans.length;
          }
          freq[s[start]]--;
          start++;
      }
  }
  return ans; 
};
