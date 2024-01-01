
'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites 
where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

Return the ordering of courses you should take to finish all courses. 
If there are many valid answers, return any of them. 
If it is impossible to finish all courses, return an empty array. 
'''

# https://leetcode.com/problems/course-schedule-ii/description/

from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        n = numCourses
        adj = [[] for _ in range(n)]
        indeg = [0 for _ in range(n)]
        for a,b in prerequisites:
            adj[b].append(a)
            indeg[a] += 1
        q = deque()
        topo = []
        for i,d in enumerate(indeg):
            if not d:
                q.append(i)
        while q:
            a = q.popleft()
            topo.append(a)
            for b in adj[a]:
                indeg[b] -= 1
                if not indeg[b]:
                    q.append(b)
        if len(topo) != n:
            return []
        return topo