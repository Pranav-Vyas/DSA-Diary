'''
problem - https://practice.geeksforgeeks.org/problems/path-with-minimum-effort/1
'''

# Dijkstra's algo

from heapq import *

class Solution:
    def MinimumEffort(self, a):
        n = len(a)
        m = len(a[0])
        pq = []
        mat = [[float('inf') for i in range(m)] for j in range(n)]
        mat[0][0] = 0
        pq.append((0,0))
        delRow = [0,1,0,-1]
        delCol = [1,0,-1,0]
        while pq:
            x,y = heappop(pq)
            if x == n-1 and y == m-1:
                return mat[x][y]
            for k in range(4):
                p,q = x+delRow[k],y+delCol[k]
                if p>=0 and p<n and q>=0 and q<m and mat[p][q] > max(mat[x][y], abs(a[x][y] - a[p][q])):
                    mat[p][q] = max(mat[x][y], abs(a[x][y] - a[p][q]))
                    heappush(pq, (p,q))
        return 0