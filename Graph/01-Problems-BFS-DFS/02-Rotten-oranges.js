
// https://leetcode.com/problems/rotting-oranges/description/

var orangesRotting = function(grid) {
  let n = grid.length;
  let m = grid[0].length;
  let q = new Dequeue();
  for (let i = 0; i<n; i++){
      for (let j = 0; j<m; j++){
          if (grid[i][j] === 2){
              q.push([i,j]);
          }
      }
  }
  let time = 0;
  let delRow = [0,1,0,-1];
  let delCol = [1,0,-1,0];
  function isValid(i,j){
      if (i<0 || i>=n || j<0 || j>=m) return false;
      return true;
  }
  while (q.size){
      let n = q.size;
      while (n){
          let [i,j] = q.front();
          q.popleft();
          for (let x = 0; x<4; x++){
              if (isValid(i+delRow[x], j+delCol[x]) && grid[i+delRow[x]][j+delCol[x]] === 1){
                  grid[i+delRow[x]][j+delCol[x]] = 2;
                  q.push([i+delRow[x], j+delCol[x]]);
              }
          }
          n--;
      }
      if (q.size){
          time++;
      }
  }
  let hasFreshOranges = false;
  grid.forEach(arr => {
      arr.forEach(x => {
          if (x === 1) {
              hasFreshOranges = true;
          }
      });
  });

  if (hasFreshOranges) {
      return -1;
  }
  return time;
};

/**
Python

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        cells = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cells.add((i,j))
                elif grid[i][j] == 2:
                    q.append((i,j))
        ans = 0
        while q:
            n = len(q)
            while n:
                i,j = q.popleft()
                if (i+1,j) in cells:
                    cells.remove((i+1,j))
                    q.append((i+1,j))
                if (i-1,j) in cells:
                    cells.remove((i-1,j))
                    q.append((i-1,j))
                if (i,j+1) in cells:
                    cells.remove((i,j+1))
                    q.append((i,j+1))
                if (i,j-1) in cells:
                    cells.remove((i,j-1))
                    q.append((i,j-1))
                n -= 1
            ans += len(q) > 0
        if len(cells) > 0:
            return -1
        return ans
                

*/