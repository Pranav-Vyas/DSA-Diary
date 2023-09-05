/*
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, 
and the sign represents its direction (positive meaning right, negative meaning left). 
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. 
If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet. 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
*/

// time - O(n)
// space - O(n)

var asteroidCollision = function(arr) {
  const n = arr.length;
  const s = [];
  arr.forEach((ast, i) => {
      let flag = false
      while (s.length && (arr[s[s.length-1]] * ast) < 0 && arr[s[s.length-1]] > 0 && ast < 0 ){
          if (Math.abs(ast) === Math.abs(arr[s[s.length-1]])){
              s.pop();
              flag = true;
              break;
          } else if (Math.abs(ast) < Math.abs(arr[s[s.length-1]])){
              flag = true;
              break;
          } else {
              s.pop();
          }
      }
      if (!flag){
          s.push(i);
      }
  })
  return s.map(i => arr[i]);
};