'''
You are given an n x n binary grid. A grid is said to be binary if every value in grid is either 1 or 0.

You can change at most one cell in grid from 0 to 1.

You need to find the largest group of connected  1's.

Two cells are said to be connected if both are adjacent to each other and both have same value.

Input:
2
1 1
0 1

Output:
4

problem - https://practice.geeksforgeeks.org/problems/maximum-connected-group/1
'''

from typing import List

class Solution:
    def MaxConnection(self, grid : List[List[int]]) -> int:
        n = len(grid) * len(grid)
        size = [1 for i in range(n)]
        parent = [i for i in range(n)]
        delRow = [1,0,-1,0]
        delCol = [0,1,0,-1]
        
        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]
            
        def union(u,v):
            pu = find(u)
            pv = find(v)
            if pu == pv:
                return
            if size[pu] > size[pv]:
                parent[pv] = pu
                size[pu] += size[pv]
            elif size[pu] < size[pv]:
                parent[pu] = pv
                size[pv] += size[pu]
            else:
                parent[pv] = pu
                size[pu] += size[pv]
        
        def getPos(u,v):
            return (u*len(grid)) + v
            
        def isValid(u,v):
            if u<0 or u>=len(grid) or v<0 or v>=len(grid):
                return False
            return True
            
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]:
                    if isValid(i-1,j) and grid[i-1][j]:
                        union(getPos(i,j), getPos(i-1,j))
                    if isValid(i,j-1) and grid[i][j-1]:
                        union(getPos(i,j), getPos(i,j-1))
        
        ans = max(1, max(size))
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if not grid[i][j]:
                    st = set()
                    for k in range(4):
                        x, y = i+delRow[k], j+delCol[k]
                        if isValid(x,y) and grid[x][y]:
                            st.add(find(getPos(x,y)))
                    count = 1
                    for p in st:
                        count += size[p]
                    ans = max(ans,count)
        return ans