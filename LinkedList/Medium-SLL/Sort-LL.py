
'''
Sort LL in non-decreasing order in O(nlogn) time and O(1) space
'''

# Merge sort - recursion
# time = O( n * logn) and space = O( logn )

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def sortList(self, head):
    def findMid(head):
      pre = None
      slow = fast = head
      while fast and fast.next:
          slow, pre, fast = slow.next, slow, fast.next.next
      pre.next = None
      return slow
    
    def merge(head1, head2):
      cur1 = head1
      cur2 = head2
      temp = head = ListNode()
      while cur1 and cur2:
        if cur1.val <= cur2.val:
          temp.next = cur1
          cur1 = cur1.next
          temp = temp.next
        else:
          temp.next = cur2
          cur2 = cur2.next
          temp = temp.next
      temp.next = cur1 if cur1 else cur2
      return head.next
    
    def mergeSort(head):
      if not head or not head.next:
        return head
      mid = findMid(head)
      left = mergeSort(head)
      right = mergeSort(mid)
      return merge(left, right)
        
    return mergeSort(head)

# for O(1) space, see leetcode solutions of others
# https://leetcode.com/problems/sort-list/solutions/