
'''
Delete all occurrences of a given key in a doubly linked list

Example
DLL = 10 -> 20 -> 10 -> 30 -> 10
answer = 20 -> 30
'''

class Node:
  def __init__(self, data=0, next=None, prev=None):
    self.data = data
    self.next = next
    self.prev = prev

def deleteAllOccurrences(head: Node, k: int) -> Node:
  cur = head
  while cur:
    if cur.data == k:
      temp = cur
      if cur.prev:
          cur.prev.next = cur.next
      if cur.next:
          cur.next.prev = cur.prev
      if cur == head:
          head = head.next
      del temp
    cur = cur.next
  return head

# time = O(n)
# space = O(1)