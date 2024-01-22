# https://leetcode.com/problems/hand-of-straights/

'''
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, 
and consists of groupSize consecutive cards.
Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
'''

# Intuition
'''
- take one ele from heap and check if we can put all elements in a new group starting from that ele.
- alongside reduce frequency of cosecutive elements
'''

from collections import defaultdict
import heapq
class Solution:
    def isNStraightHand(self, hand, groupSize):
        k=groupSize
        if k==1:
            return True
        n=len(hand)
        if n%k:
            return False
        h=defaultdict(int)
        for i in hand:
            h[i]+=1
        heapq.heapify(hand)
        for i in range(n//k):
            start=heapq.heappop(hand)
            while h[start]==0 and hand:
                start=heapq.heappop(hand)
            for l in range(k):
                h[start]-=1
                if h[start]<0:
                    return False
                start+=1
        return True