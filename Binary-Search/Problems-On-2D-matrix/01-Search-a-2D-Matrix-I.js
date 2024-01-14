// Problem - https://leetcode.com/problems/search-a-2d-matrix/description/

var searchMatrix = function(mat, tar) {
  let n = mat.length;
  let m = mat[0].length;
  let low = 0;
  let high = (n*m)-1;
  while (low <= high){
      let mid = Math.floor((low+high)/2);
      let row = Math.floor(mid/m);
      let col = mid - (row * m);
      if (mat[row][col] == tar){
          return true;
      } else if (mat[row][col] < tar){
          low = mid + 1;
      } else {
          high = mid - 1;
      }
  }
  return false;
};

// Search a 2D matrix II
// https://leetcode.com/problems/search-a-2d-matrix-ii/description/