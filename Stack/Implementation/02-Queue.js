
// 2 types - 

// 1. queue
// 2. doubly ended queue (DE-Queue)

/**
 * Operations - dequeue
 * 
 * pop
 * popleft
 * push
 * pushleft
 * front - optional
 * back - optional
 * print - optional
 * size - optional
 */

/**
 * Methods
 * 
 * 1. linkedlist
 * 2. arrays
 * 3. stacks
 */

// Method 1 linked list

function Node(val, pre, next){
  this.val = val;
  this.pre = pre === undefined ? null : pre;
  this.next = next === undefined ? null : next;
}

function Dequeue(){
  this.head = null;
  this.tail = null;
  this.size = 0;

  this.push = function(val){
      let node = new Node(val);
      if (this.tail){
          this.tail.next = node;
          node.pre = this.tail;
          this.tail = this.tail.next;
      } else {
          this.head = this.tail = node;
      }
      this.size++;
  }

  this.pop = function() {
      if (this.size){
          if (this.size === 1){
              this.head = this.tail = null;
          } else {
              this.tail = this.tail.pre;
              this.tail.next = null;
          }
          this.size--;
      }
  }

  this.popleft = function() {
      if (this.size){
          if (this.size === 1){
              this.head = this.tail = null;
          } else {
              this.head = this.head.next;
              this.head.pre = null;
          }
          this.size--;
      }
  }

  this.pushleft = function(val){
      let node = new Node(val);
      if (this.tail){
          node.next = this.head;
          this.head.pre = node;
          this.head = node;
      } else {
          this.head = this.tail = node;
      }
      this.size++;
  }

  this.front = function(){
      return this.head ? this.head.val : null;
  }

  this.back = function(){
      return this.tail ? this.tail.val : null;
  }

  this.print = function(){
      let temp = this.head;
      let s = "";
      while (temp){
          s += String(temp.val) + " ";
          temp = temp.next;
      }
      console.log(s);
  }
}