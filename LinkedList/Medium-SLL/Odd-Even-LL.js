
/*
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, 
and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
*/

var oddEvenList = function(head) {
  if (!head || !head.next) return head;
  let head1 = head;
  let head2 = head.next;
  let cur1 = head;
  let cur2 = head.next;
  while (cur2 && cur2.next){
      cur1.next = cur2.next;
      cur1 = cur1.next;
      cur2.next = cur2.next.next;
      cur2 = cur2.next;
  }
  cur1.next = head2;
  return head1;
};

