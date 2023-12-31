"""
Leetcode
1046. Last Stone Weight (easy)
2022-04-07

You are given an array of integers stones where stones[i] is the weight 
of the ith stone.

We are playing a game with the stones. On each turn, we choose the 
heaviest two stones and smash them together. Suppose the heaviest two 
stones have weights x and y with x <= y. The result of this smash is:

 - If x == y, both stones are destroyed, and
 - If x != y, the stone of weight x is destroyed, and the stone of weight 
   y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no 
stones left, return 0.
"""

from typing import List



# try 1
# Runtime: 50 ms, faster than 36.93% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 13.9 MB, less than 68.03% of Python3 online submissions for Last Stone Weight.
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            y = stones.pop(stones.index(max(stones)))
            x = stones.pop(stones.index(max(stones)))
            if y > x: stones.append(y - x)
            
        return stones[0] if stones else 0


# priority queue
# Runtime: 56 ms, faster than 22.77% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 14 MB, less than 17.07% of Python3 online submissions for Last Stone Weight.
class Solution1:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        from queue import PriorityQueue

        if not stones: return stones
        if len(stones) == 1: return stones[0]

        pq = PriorityQueue()
        for n in stones: pq.put(-n)

        while pq.qsize() > 1:
            x = pq.get()
            y = pq.get()
            if -x > -y: pq.put(x - y)
            
        return -pq.get() if pq.qsize() > 0 else 0



s = Solution1()
tests = [
    [2,2],
    [2,7,4,1,8,1],
    [1]
]
for t in tests:
    print(t)
    print(s.lastStoneWeight(t))
    print()
