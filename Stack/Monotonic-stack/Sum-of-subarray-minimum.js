// Sum of subarray minimum

/*
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. 
Since the answer may be large, 
return the answer modulo 109 + 7.
*/

/*
Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
*/

// Trick

/*
- for each element, check in how many subarray can it be used as minimum.
- Next Smaller Element on left and right
*/

// 1. Using 2 passes

var sumSubarrayMins = function(arr) {
  const n = arr.length;
  const left = Array.from({length: n}, () => -1);
  const right = Array.from({length: n}, () => n);
  let s = [];
  let ans = 0;
  arr.forEach((x,i) => {
      while (s.length && arr[s[s.length-1]] >= arr[i]){
          right[s.pop()] = i;
      }
      s.push(i);
  })
  s = [];
  for (let i = n-1; i >= 0; i--){
      while (s.length && arr[s[s.length-1]] > arr[i]){
          left[s.pop()] = i;
      }
      s.push(i);
  }
  arr.forEach((x,i) => {
      ans += ( x * (right[i] - i) * (i - left[i]) ) % 1000000007
  })
  return ans % 1000000007;
};

// 2. Using 1 pass

var sumSubarrayMins = function(arr) {
  const n = arr.length;
  if (n === 1) {
      return arr[0];
  }
  const stack = [];
  const left = Array(n).fill(-1);
  const right = Array(n).fill(n);
  const m = 10 ** 9 + 7;

  for (let i = 0; i < n; i++) {
      while (stack.length > 0 && arr[i] <= arr[stack[stack.length - 1]]) {
          const temp = stack.pop();
          right[temp] = i;
      }
      left[i] = stack.length > 0 ? stack[stack.length - 1] : -1;
      stack.push(i);
  }

  let ans = 0;
  for (let i = 0; i < n; i++) {
      ans += arr[i] * (i - left[i]) * (right[i] - i);
  }

  return ans % m;
};

