/*
Given the head of a linked list, return the node where the cycle begins. 
If there is no cycle, return null.
*/

/*
20 ----> 10 ----> 30 ----> 50 ----> 10
                   |                 |
                   |                 |
                  60 ----> 25 ----> 20

answer = index 2
*/

/*
- follow slow and fast algo
- if slow and fast meet, then there is a cycle
- the 'head' and 'slow'/'fast' are at same distance from 'starting point of cycle'
- calculate that distance
*/

var detectCycle = function(head) {
  if (!head) return null;
  let slow = head, fast = head;
  let isCycle = false;
  while (fast && fast.next){
      slow = slow.next;
      fast = fast.next.next;
      if (slow === fast) {
          isCycle = true;
          break;
      }
  }
  if (!isCycle) return null;
  slow = head;
  while (slow !== fast){
      slow = slow.next;
      fast = fast.next;
  }
  return slow;
}