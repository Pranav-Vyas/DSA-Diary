# problem - https://practice.geeksforgeeks.org/problems/number-of-islands/1

from typing import List
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        mat = [[0 for i in range(cols)] for j in range(rows)]
        count = 0
        delRow = [1,0,-1,0]
        delCol = [0,1,0,-1]
        res = []
        n = rows * cols
        parent = [i for i in range(n)]
        rank = [0 for i in range(n)]
        
        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]
            
        def union(u,v):
            pu = find(u)
            pv = find(v)
            if pu == pv:
                return
            if rank[pu] > rank[pv]:
                parent[pv] = pu
            elif rank[pu] < rank[pv]:
                parent[pu] = pv
            else:
                parent[pv] = pu
                rank[pu] += 1
                
        def getPos(u,v):
            return (u*cols) + v
            
        for u,v in operators:
            if mat[u][v]:
                res.append(count)
            else:
                mat[u][v] = 1
                count += 1
                for k in range(4):
                    x,y = u+delRow[k],v+delCol[k]
                    if x>=0 and x<rows and y>=0 and y<cols and mat[x][y]:
                        pos1 = getPos(x,y)
                        pos2 = getPos(u,v)
                        p1 = find(pos1)
                        p2 = find(pos2)
                        if p1 != p2:
                            union(p1,p2)
                            count -= 1
                res.append(count)
        return res