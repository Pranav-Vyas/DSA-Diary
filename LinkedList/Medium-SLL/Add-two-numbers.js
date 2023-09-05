
/*
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
*/

function ListNode(val, next) {
  this.val = (val === undefined ? 0 : val)
  this.next = (next === undefined ? null : next)
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  function recur(h1, h2, cary) {
    if (!h1 && !h2) {
      if (cary) {
        return new ListNode(cary);
      }
      return null;
    }
    else if (!h2) {
      let s = h1.val;
      s += cary;
      let node = new ListNode(s % 10);
      node.next = recur(h1.next, h2, Math.floor(s / 10));
      return node;
    } else if (!h1) {
      let s = h2.val;
      s += cary;
      let node = new ListNode(s % 10);
      node.next = recur(h1, h2.next, Math.floor(s / 10));
      return node;
    } else {
      let s = h1.val + h2.val;
      s += cary;
      let node = new ListNode(s % 10);
      node.next = recur(h1.next, h2.next, Math.floor(s / 10));
      return node;
    }
  }
  return recur(l1, l2, 0)
};