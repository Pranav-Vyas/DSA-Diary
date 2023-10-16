
'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.
'''

# https://leetcode.com/problems/01-matrix/description/

from collections import deque
class Solution:
    def updateMatrix(self, mat):
        n = len(mat)
        m = len(mat[0])
        q = deque()
        visited = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i,j))
                    visited[i][j] = 1
        arr = [[0 for j in range(m)] for i in range(n)]
        dist = 0
        row = [0,1,0,-1]
        col = [1,0,-1,0]
        def isValid(i,j):
            if i<0 or i>=n or j<0 or j>=m:
                return False
            return True
        while q:
            l = len(q)
            while l:
                i,j = q.popleft()
                arr[i][j] = dist
                for k in range(4):
                    if isValid(i+row[k], j+col[k]) and not visited[i+row[k]][j+col[k]]:
                        q.append((i+row[k], j+col[k]))
                        visited[i+row[k]][j+col[k]] = 1
                l -= 1
            dist += 1
        return arr

                    