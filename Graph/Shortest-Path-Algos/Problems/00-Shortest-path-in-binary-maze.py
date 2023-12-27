'''
Given a binary maze of 0 and 1
given src and dest
find the shortest path from source and dest
distance between adjacent cells is 1

problem - https://practice.geeksforgeeks.org/problems/shortest-path-in-a-binary-maze-1655453161/1
'''

# Disjkstra algo but with queue not priority queue
# because distance between all adjacent cells is same
# so no additional benefit from PQ

from collections import deque

class Solution:
    
    def shortestPath(self, grid, src, dest) -> int:
        n = len(grid)
        m = len(grid[0])
        mat = [[float('inf') for i in range(m)] for j in range(n)]
        mat[src[0]][src[1]] = 0
        queue = deque()
        queue.append((src[0],src[1]))
        delRow = [0,1,0,-1]
        delCol = [1,0,-1,0]
        while queue:
            x,y = queue.popleft()
            if x == dest[0] and y == dest[1]:
                return mat[x][y]
            for k in range(4):
                p, q = x + delRow[k], y + delCol[k]
                if p >= 0 and p < n and q >= 0 and q < m and grid[p][q] != 0 and mat[p][q] > mat[x][y]+1:
                    mat[p][q] = mat[x][y]+1
                    queue.append((p,q))
        return -1