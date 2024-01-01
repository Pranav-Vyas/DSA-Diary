'''
problem - https://practice.geeksforgeeks.org/problems/city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/1
'''

# Floyd Warshall algo

class Solution:
    def findCity(self, n, m, edges, threshold):
        mat = [[float('inf') for _ in range(n)] for __ in range(n)]
        for u,v,w in edges:
            mat[u][v] = w
            mat[v][u] = w
        for i in range(n):
            mat[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
        miniV, miniC = -1,float('inf')
        for u in range(n):
            count = 0
            for w in mat[u]:
                if w <= threshold:
                    count += 1
            if count <= miniC:
                miniV = u
                miniC = count
        return miniV