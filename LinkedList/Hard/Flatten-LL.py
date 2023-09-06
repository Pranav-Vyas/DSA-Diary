
'''
LL has 2 pointers - prev, child

(i) a next pointer to the next node,

(ii) a child pointer to a linked list where this node is head.

Each of the sub-linked-list is in sorted order.

Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 
'''

class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child


def merge(head1, head2):
    cur1 = head1
    cur2 = head2
    newHead = Node(-2)
    dummy = newHead
    while cur1 and cur2:
        if cur1.data <= cur2.data:
            dummy.child = cur1
            cur1 = cur1.child
        else:
            dummy.child = cur2
            cur2 = cur2.child
        dummy = dummy.child
    dummy.child = cur1 if cur1 else cur2
    return newHead.child

def flattenLinkedList(head: Node) -> Node:
    dummy = Node(-1)
    cur = head
    while cur:
        temp = cur.next
        cur.next = None;
        dummy = merge(dummy, cur)
        cur = temp
    return dummy.child

# Solution - https://www.codingninjas.com/studio/problems/flatten-a-linked-list_1112655

# Other similar problems

# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/