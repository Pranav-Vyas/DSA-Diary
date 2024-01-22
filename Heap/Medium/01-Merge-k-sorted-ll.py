'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []
        arr = []
        h = {}
        i = 0
        for node in lists:
            if node:
                heap.append((node.val,i))
                h[(node.val,i)] = node
            i+=1
        heapq.heapify(heap)
        head = None
        cur = None
        if heap:
            val,idx = heapq.heappop(heap)
            head = cur = h[(val,idx)]
            if cur.next:
                heapq.heappush(heap,(cur.next.val,idx))
                h[(cur.next.val,idx)] = cur.next
        else:
            return None

        while heap:
            val,idx = heapq.heappop(heap)
            temp = h[(val,idx)]
            cur.next = temp
            if temp.next:
                heapq.heappush(heap,(temp.next.val,idx))
                h[(temp.next.val,idx)] = temp.next
            cur = cur.next
        
        return head