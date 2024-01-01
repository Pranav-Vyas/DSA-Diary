# problem - https://practice.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1

class Solution:
    def bellman_ford(self, V, edges, S):
        dist = [float('inf') for _ in range(V)]
        dist[S] = 0
        for _ in range(V-1):
            for u,v,w in edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u,v,w in edges:
            if dist[u] + w < dist[v]:
                return [-1]
        for i,d in enumerate(dist):
            if d == float('inf'):
                dist[i] = 100000000
        return dist

# Q. 1 Why (n-1) iterations
'''
- edges can be in any order. suppose we have 5 vertices and following order of edges
(3,4,1)   (2,3,1)   (1,2,1)   (0,1,1)

- now source is 0, therefore array of dist will be [0, INF, INF, INF, INF]
- in 1st iteration, only vertex 1 will be updated. This is because except 0, all have 'INF', 
so 3 cannot update 4, 2 cannot update 3, 1 cannot update 2, only 0 can update 1
- upto 2nd iteration, we will have vertex 1 got updated, hence it can update vertex 2
- so after n-1 iterations, we will be able to update all vertices
'''

# Q. 2 How to detect negative cycle?

'''
After n-1 iterations, on the nth iteration if dist arr got updated, then there exist one negative cycle
'''