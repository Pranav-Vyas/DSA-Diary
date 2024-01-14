// Find a peak element II

// https://leetcode.com/problems/find-a-peak-element-ii/submissions/


function getRow(mat,n,m,col){
  let idx = -1;
  let maxi = -1;
  for (let row = 0; row < n; row++){
      if (mat[row][col] > maxi){
          maxi = mat[row][col];
          idx = row;
      }
  }
  return idx;
}

/**
* @param {number[][]} mat
* @return {number[]}
*/
var findPeakGrid = function(mat) {
  let n = mat.length;
  let m = mat[0].length;
  let low = 0;
  let high = m-1;
  while (low <= high){
      let mid = Math.floor((low + high)/2);
      let row = getRow(mat,n,m,mid);
      let left = -1;
      if (mid-1 >= 0){
          left = mat[row][mid-1];
      }
      let right = -1;
      if (mid+1 < m){
          right = mat[row][mid+1];
      }
      if (mat[row][mid] > left && mat[row][mid] > right){
          return [row,mid];
      } else if (mat[row][mid] < left){
          high = mid-1;
      } else {
          low = mid+1;
      }
  }
  return [-1,-1];
};
