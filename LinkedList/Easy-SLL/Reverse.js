
// Reverse

// Iterative

var reverseList = function(head) {
  let pre = null;
  let cur = head;
  while (cur){
      let temp = cur.next;
      cur.next = pre;
      pre = cur;
      cur = temp;
  }
  return pre;
};

// Recursive

function recur(head){
  if (!head.next) return [head, head];
  let [newHead, tail] = recur(head.next);
  head.next = null;
  tail.next = head;
  return [newHead, head];
}

var reverseList = function(head) {
  if (!head) return null;
  return recur(head)[0];
};