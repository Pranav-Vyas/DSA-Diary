"""
------------------- WORD LADDER I AND II --------------------


Word ladder I
- given 'start word', 'target word' and 'word list'
- can change any one letter of word
- Find the length of the shortest transformation sequence from start to target

Input:
wordList = {"des","der","dfr","dgt","dfs"}
startWord = "der", targetWord= "dfs",

Output:
3

problem - https://practice.geeksforgeeks.org/problems/word-ladder/1

Word ladder II
- Return all possible tranformation sequences

Input:
startWord = "der", targetWord = "dfs",
wordList = {"des","der","dfr","dgt","dfs"}

Output:
der dfr dfs
der des dfs

problem - https://practice.geeksforgeeks.org/problems/word-ladder-ii/1
"""

# ---------- Word ladder I - Brute Force

from collections import deque
class Solution:
    def wordLadderLength(self, start, target, wordList):
        words = set(wordList)
        if target not in words:
            return 0
        m = len(wordList[0])
        q = deque()
        q.append(start)
        level = 1
        while q:
            size = len(q)
            while size:
                w = q.popleft()
                if w == target:
                    return level
                for i in range(m):
                    for j in range(97, 123):
                        newWord = w[:i] + chr(j) + w[i + 1 :]
                        if newWord != w and newWord in words:
                            q.append(newWord)
                size -= 1
            if len(q):
                level += 1
            return 0

# ---------- Word ladder II - Brute Force

class Solution:
  def findSequences(self, start, target, wordList):
    words = set(wordList)
    if target not in words:
      return []
    q = deque()
    m = len(wordList[0])
    found = False
    ans = []
    q.append([start])
    while q:
      size = len(q)
      while size:
          arr = q.popleft()
          w = arr[-1]
          for i in range(m):
            for j in range(97, 123):
              newWord = w[:i] + chr(j) + w[i+1:]
              if newWord != w and newWord in words:
                new_arr = arr.copy()
                new_arr.append(newWord)
                q.append(new_arr)
                if newWord == target:
                  ans.append(new_arr)
                  found = True
      size -= 1
      if found:
        return ans
    return ans