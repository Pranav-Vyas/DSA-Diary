/*
Problem Statement: Given an array of integers arr, there is a sliding window of size k 
which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. 
Each time the sliding window moves right by one position. 
Return the max of each sliding window.
*/

// Intuition

/*
- use dequeue of size <= k
- idea is to remove useless element from window and put elements which can be useful in future.
- suppose arr = [1,2,3,2,1,1]
- cur window = [1,2,3], max is 3
- when we slide window, cur = [2,3,2], max is still 3
- but if arr = [1,2,3,4,1,1], if cur = [2,3,4], max = 4
- due to 4, 3 cannot be maximum in any of the upcoming windows, so 3 is useless
*/

// Process

/*
- q = dequeue()
- front of 'q' is max of cur window
- when adding new element, pop every element of 'q' which is less than new element.
- also check for element going out of window.
*/

function Dequeue(){
  // implemented before
}

var maxSlidingWindow = function(nums, k) {
  const queue = new Dequeue();
  const ans = [];
  const n = nums.length;
  // cal max of first window
  for (let i = 0; i < k; i++){
      while (queue.size && nums[queue.back()] < nums[i]){
          queue.pop();
      }
      queue.push(i);
  }
  ans.push(nums[queue.front()]);
  i = 1;
  j = k;
  while (j < n){
      // remove element out of new window
      while (queue.size && queue.front() < i){
          queue.popleft();
      }
      // monotonic queue
      while (queue.size && nums[queue.back()] < nums[j]){
          queue.pop();
      }
      queue.push(j);
      ans.push(nums[queue.front()]);
      i++;
      j++;
  }
  return ans;
};
