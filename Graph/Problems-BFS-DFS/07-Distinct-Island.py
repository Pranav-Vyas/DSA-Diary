'''
Given a boolean 2D matrix grid of size n * m. 
You have to find the number of distinct islands where a group of connected 1s (horizontally or vertically) forms an island. 
Two islands are considered to be distinct if and only if one island is not equal to another (not rotated or reflected).
'''
# https://practice.geeksforgeeks.org/problems/number-of-distinct-islands/1

class Solution:
    def countDistinctIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        visited = [[False for j in range(m)] for i in range(n)]
        ans = set()
        row = [-1,0,1,0]
        col = [0,-1,0,1]
        def isValid(i,j):
            if i<0 or i>= n or j<0 or j==m:
                return False
            return True
        def dfs(i, j, row0, col0, res = []):
            visited[i][j] = True
            res.append((row0-i, col0-j))
            for k in range(4):
                u = i+row[k]
                v = j+col[k]
                if isValid(u,v) and not visited[u][v] and grid[u][v] == 1:
                    dfs(u,v,row0,col0,res)
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == 1:
                    res = []
                    dfs(i,j,i,j,res)
                    ans.add(tuple(res))
        return len(ans)
    
# Equivalent JavaScript code
# use Json.stringify to convert into unique value in set

'''
class Solution {
    countDistinctIslands(grid) {
        const n = grid.length;
        const m = grid[0].length;
        const visited = new Array(n).fill(false).map(() => new Array(m).fill(false));
        const ans = new Set();
        const row = [-1, 0, 1, 0];
        const col = [0, -1, 0, 1];

        function isValid(i, j) {
            return i >= 0 && i < n && j >= 0 && j < m;
        }

        function dfs(i, j, row0, col0, res = []) {
            visited[i][j] = true;
            res.push([row0 - i, col0 - j]);
            for (let k = 0; k < 4; k++) {
                const u = i + row[k];
                const v = j + col[k];
                if (isValid(u, v) && !visited[u][v] && grid[u][v] === 1) {
                    dfs(u, v, row0, col0, res);
                }
            }
        }

        for (let i = 0; i < n; i++) {
            for (let j = 0; j < m; j++) {
                if (!visited[i][j] && grid[i][j] === 1) {
                    const res = [];
                    dfs(i, j, i, j, res);
                    ans.add(JSON.stringify(res)); // Using JSON.stringify to create a unique representation of the island
                }
            }
        }

        return ans.size;
    }
}

'''