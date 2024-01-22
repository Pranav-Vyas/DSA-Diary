# https://leetcode.com/problems/find-median-from-data-stream/

'''
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
'''

from heapq import heappop, heappush, heappushpop
class MedianFinder:

    def __init__(self):
        # self.arr = []
        self.maxh = []
        self.minh = []

    def addNum(self, num: int) -> None:
        if len(self.maxh) == len(self.minh):
            heappush(self.minh,-heappushpop(self.maxh,-num))
        else:
            heappush(self.maxh,-heappushpop(self.minh,num))

    def findMedian(self) -> float:
        # n = len(self.arr)
        # print(self.maxh,self.minh)
        if len(self.maxh) == len(self.minh):
            return float((-self.maxh[0] + self.minh[0])/2)
        else:
            return float(self.minh[0])
        

# Other Medium problems
# Connect `n` ropes with minimal cost
# Maximum Sum Combination
# k most frequent element