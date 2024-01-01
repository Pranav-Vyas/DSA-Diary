
// https://leetcode.com/problems/flood-fill/description/

var floodFill = function(image, sr, sc, color) {
  let ans = image.map(x => x.map(y => y));
  let n = ans.length;
  let m = ans[0].length;
  let oldColor = image[sr][sc];
  let delRow = [-1,0,1,0];
  let delCol = [0,-1,0,1];
  function isValid(i,j){
    if (i < 0 || i >= n || j < 0 || j >= m) return false;
    return true;
  }
  function dfs(i,j){
    for (let x = 0; x<4; x++){
      if (isValid(i+delRow[x], j+delCol[x]) && image[i+delRow[x]][j+delCol[x]] === oldColor && ans[i+delRow[x]][j+delCol[x]] !== color){
        ans[i+delRow[x]][j+delCol[x]] = color;
        dfs(i+delRow[x], j+delCol[x]);
      }
    }
  }
  ans[sr][sc] = color;
  dfs(sr,sc);
  return ans;
};