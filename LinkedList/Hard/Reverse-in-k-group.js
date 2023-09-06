/*
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
*/

function reverse(head){
  let pre = null;
  let cur = head;
  let newHead;
  while (cur) {
      temp = cur.next;
      cur.next = pre;
      pre = cur;
      cur = temp;
      if (!temp){
          newHead = pre;
      }
  }
  return [newHead, head];
}

var reverseKGroup = function(head, k) {
  let newHead = head;
  let cur = head;
  let pre = null;
  while (cur) {
      let len = k-1;
      let start = cur;
      let end = cur;
      while (end.next && len) {
          end = end.next;
          len--;
      }
      if (len){
          return newHead;
      }
      let next = end.next;
      end.next = null;
      let [curHead, curTail] = reverse(start);
      if (!pre){
          newHead = curHead;
      } else {
          pre.next = curHead;
      }
      pre = curTail;
      curTail.next = next;
      cur = next;
  }
  return newHead;
};