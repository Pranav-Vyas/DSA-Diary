# problem - https://practice.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1

'''
- calc dist between every two vertices via every vertex
'''

class Solution:
    def shortest_distance(self, mat):
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if mat[i][j] == -1:
                    mat[i][j] = float("inf")
                if i == j:
                    mat[i][j] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
        for i in range(n):
            for j in range(n):
                if mat[i][j] == float("inf"):
                    mat[i][j] = -1
        return mat
