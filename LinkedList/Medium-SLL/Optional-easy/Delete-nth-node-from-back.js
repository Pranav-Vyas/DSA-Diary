
/*
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
*/

var removeNthFromEnd = function(head, n) {
  let ahead = head;
  while (n){
      ahead = ahead.next;
      n--;
  }
  // corner case
  if (!ahead) return head.next; // it means if n == length of LL, remove 1st node
  cur = head;
  pre = null;
  while (ahead){
      pre = cur;
      cur = cur.next;
      ahead = ahead.next;
  }
  pre.next = cur.next;
  return head;
};
