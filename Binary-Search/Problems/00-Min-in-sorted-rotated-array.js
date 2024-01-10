/**
Given the sorted rotated array nums of unique elements, return the minimum element of this array.

Input: nums = [3,4,5,1,2]
Output: 1
*/

// Identify the sorted half and take min of that sorted half and then eliminate it.

var findMin = function(nums) {
  let ans = Infinity;
  let i = 0;
  let j = nums.length-1;
  while (i <= j){
      let m = Math.floor((i+j)/2);
      if (nums[i] <= nums[m]){
          ans = Math.min(ans,nums[i]);
          i = m+1;
      } else {
          ans = Math.min(ans,nums[m]);
          j = m-1;
      }
  }
  return ans;
};