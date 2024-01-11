
// https://www.geeksforgeeks.org/problems/aggressive-cows/0

class Solution {
  solve(n, k, stalls) {
      stalls.sort(function(a, b) { // normal sort() will sort based on string values
          return a - b;
      });
      function check(dist){
          let count = 1;
          let pre = 0;
          for (let i = 1; i<n; i++){
              if (Math.abs(stalls[i] - stalls[pre]) < dist){
                  continue;
              }
              count++;
              pre = i;
          }
          return count >= k;
      }
      let low = 1;
      let high = stalls.reduce((acc,cur) => Math.max(acc,cur),1);
      let ans = 1;
      while (low <= high){
          let m = Math.floor((low+high)/2);
          if (check(m)){
              ans = m;
              low = m+1;
          } else {
              high = m-1;
          }
      }
      return ans;
  }
}
