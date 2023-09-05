
// Problem - https://leetcode.com/problems/largest-rectangle-in-histogram/description/

/*
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.
*/

// Trick - Next smaller element
// O(n)

var largestRectangleArea = function(arr) {
  const n = arr.length;
  const right = Array.from({length: n}, () => n);
  const left = Array.from({length: n}, () => -1);
  let stack = [];
  for (let i = 0; i < n; i++){
      while (stack.length && arr[stack[stack.length-1]] > arr[i]){
          let idx = stack.pop();
          right[idx] = i; // smaller element on right
      }
      stack.push(i);
  }
  for (let i = n-1; i >= 0; i--){
      while (stack.length && arr[stack[stack.length-1]] > arr[i]){
          let idx = stack.pop();
          left[idx] = i; // smaller on left
      }
      stack.push(i);
  }
  let ans = 0;
  for (let i = 0; i<n; i++){
      ans = Math.max(ans, (right[i] - left[i] - 1)*arr[i]);
  }
  return ans;
};


// More questions
// - Maximum rectangle - https://leetcode.com/problems/maximal-rectangle/