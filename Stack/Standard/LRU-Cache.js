
/*
Problem Statement: “Design a data structure that follows the constraints of Least Recently Used (LRU) cache”.

Implement the LRUCache class:

- LRUCache(int capacity) we need to initialize the LRU cache with positive size capacity.
- int get(int key) returns the value of the key if the key exists, otherwise return -1.
- Void put(int key,int value), Update the value of the key if the key exists. 
  Otherwise, add the key-value pair to the cache.if the number of keys exceeds the capacity from this operation, 
  evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
*/



function Node(key = -1, val = -1){
  this.key = key;
  this.val = val;
  this.pre = null;
  this.next = null;
}

var LRUCache = function(capacity) {
  this.cap = capacity;
  this.map = {};
  this.size = 0;
  this.head = new Node(-1,-1);
  this.tail = new Node(-1,-1);
  this.head.next = this.tail;
  this.tail.pre = this.head;
};

/** 
* @param {number} key
* @return {number}
*/
LRUCache.prototype.get = function(key) {
  if (this.map[key] !== undefined){
      let node = this.map[key];
      [node.pre.next, node.next.pre] = [ node.next, node.pre];
      node.pre = this.head;
      node.next = this.head.next;
      this.head.next = node;
      node.next.pre = node;
      return node.val;
  }
  return -1;
};

/** 
* @param {number} key 
* @param {number} value
* @return {void}
*/
LRUCache.prototype.put = function(key, value) {
  let node = new Node(key, value);
  if (this.map[key] !== undefined){
      let old = this.map[key];
      [old.pre.next, old.next.pre] = [ old.next, old.pre]
  } else {
      this.size++;
  }
  this.map[key] = node;
  node.next = this.head.next;
  node.next.pre = node;
  this.head.next = node;
  node.pre = this.head;
  if (this.size > this.cap){
      let temp = this.tail.pre;
      [temp.pre.next, temp.next.pre] = [ temp.next, temp.pre]
      delete this.map[temp.key];
      this.size--;
  }
};