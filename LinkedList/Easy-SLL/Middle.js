
/*
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
*/

// Trick - slow/fast algo or tortoise/hair algo

var middleNode = function(head) {
  let slow = head;
  let fast = head;
  while (fast && fast.next){
      slow = slow.next;
      fast = fast.next.next;
  }
  return slow;
};

/*
Other questions

- Detect cycle in linkedlist
  - using slow - fast
  - using hashmap

- Check if LL is palindrome
  - find middle of LL
  - reverse the LL from the middle
  - traverse to check if corresponding nodes have same value

*/