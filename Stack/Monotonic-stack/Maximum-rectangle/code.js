
function largestRectangleArea(arr) {
  // already implemented
}

var maximalRectangle = function(mat) {
  const n = mat.length;
  const m = mat[0].length;
  arr = Array.from({length: m}, () => 0);
  let ans = largestRectangleArea(arr);
  for (let i = 0; i < n; i++){
      for (let j = 0; j < m; j++){
          if (mat[i][j] === '1'){
              arr[j] += 1;
          } else {
              arr[j] = 0;
          }
      }
      ans = Math.max(ans, largestRectangleArea(arr));
  }
  return ans;
};

// time = O(n*m*m)
// space = O(m)