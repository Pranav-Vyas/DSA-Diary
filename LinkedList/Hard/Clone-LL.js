
/*
Clone a LL with random pointer.
The LL has 2 pointers - next and random
*/

// time = O(n)
// space = O(1)


// Definition for a Node.
function Node(val, next, random) {
   this.val = val;
   this.next = next;
   this.random = random;
};


/**
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList = function(head) {
  if (!head) return null;
  let cur = head;
  while (cur){
      let node = new Node(cur.val);
      node.next = cur.next;
      cur.next = node;
      cur = cur.next.next;
  }
  cur = head;
  while (cur){
      cur.next.random = cur.random !== null ? cur.random.next : null;
      cur = cur.next.next;
  }
  let newHead = head.next;
  cur = head;
  while (cur && cur.next){
      let temp = cur.next;
      cur.next = cur.next.next;
      cur = temp
  }
  return newHead;
};

