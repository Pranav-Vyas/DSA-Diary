'''
You are given a LL, add 1 to the the number formed by LL and return new LL

Example
LL =  1 -> 5 -> 2
newLL =  1 -> 5 -> 3
'''

class Node:
  def __init__(self, data=0, next=None):
    self.data = data
    self.next = next

def addOne(head: Node) -> Node:
  def recur(node):
    if not node.next:
      val = node.data + 1
      node.data = val % 10
      return node, val // 10
    cur, cary = recur(node.next)
    node.next = cur
    val = node.data + cary
    node.data = val % 10
    return node, val // 10
  node, cary = recur(head)
  newHead = node
  if cary:
    newHead = Node(cary)
    newHead.next = node
  return newHead