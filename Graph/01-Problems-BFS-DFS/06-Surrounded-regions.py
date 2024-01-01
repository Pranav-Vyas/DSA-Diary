'''
Given an m x n matrix board containing 'X' and 'O', 
capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''

# https://leetcode.com/problems/surrounded-regions/description/

from collections import deque

class Solution:
    def solve(self, board):
        n = len(board)
        m = len(board[0])
        visited = [[False for i in range(m)] for j in range(n)]
        row = [1,0,-1,0]
        col = [0,1,0,-1]
        def isCorner(i,j):
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                return True
            return False
        def isValid(i,j):
            if i < 0 or i > n-1 or j < 0 or j > m-1:
                return False
            return True
        def bfs(i,j):
            toChange = []
            q = deque()
            q.append((i,j))
            visited[i][j] = True
            flag = False
            while q:
                x,y = q.popleft()
                toChange.append((x,y))
                if isCorner(x,y):
                    flag = True
                for k in range(4):
                    if isValid(x+row[k], y+col[k]) and not visited[x+row[k]][y+col[k]] and board[x+row[k]][y+col[k]] == "O":
                        q.append((x+row[k], y+col[k]))
                        visited[x+row[k]][y+col[k]] = True
            if not flag:
                for u,v in toChange:
                    board[u][v] = "X"
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and not visited[i][j]:
                    bfs(i,j)


