/*
Given an array, for every element, find the next greater element on right.
*/

/*

- monotonic stack
- for new element, pop from stack untill stack's top is greater or less than new ele.
- for each poped ele, the NGE is new ele.
*/

// ****** Circular Array *******************

/*
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
return the next greater number for every element in nums.
*/

var nextGreaterElements = function(nums) {
  let arr = [...nums, ...nums];
  let stack = [];
  const n = nums.length;
  let ans = Array.from({length: n}, () => -1);
  arr.forEach((x,i) => {
      while (stack.length && nums[stack[stack.length-1]%n] < x){
          ans[stack.pop()%n] = x;
      }
      stack.push(i);
  })
  return ans;
};