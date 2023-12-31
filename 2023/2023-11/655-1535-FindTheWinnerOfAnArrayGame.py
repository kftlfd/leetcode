"""
Leetcode
1535. Find the Winner of an Array Game (medium)
2023-11-05

Given an integer array arr of distinct integers and an integer k.

A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0, and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.

Return the integer which will win the game.

It is guaranteed that there will be a winner of the game.

 

Example 1:

Input: arr = [2,1,3,5,4,6,7], k = 2
Output: 5
Explanation: Let's see the rounds of the game:
Round |       arr       | winner | win_count
  1   | [2,1,3,5,4,6,7] | 2      | 1
  2   | [2,3,5,4,6,7,1] | 3      | 1
  3   | [3,5,4,6,7,1,2] | 5      | 1
  4   | [5,4,6,7,1,2,3] | 5      | 2
So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.

Example 2:

Input: arr = [3,2,1], k = 10
Output: 3
Explanation: 3 will win the first 10 rounds consecutively.

 

Constraints:

    2 <= arr.length <= 10^5
    1 <= arr[i] <= 10^6
    arr contains distinct integers.
    1 <= k <= 10^9
"""

from typing import List
from collections import deque


class Solution:
    """
    Runtime: 4774 ms, faster than 5.43% of Python3 online submissions for Find the Winner of an Array Game.
    Memory Usage: 30 MB, less than 63.04% of Python3 online submissions for Find the Winner of an Array Game.
    """

    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)

        winner = None
        streak = 0

        while streak < k:
            cur_winner, i = max((arr[0], 0), (arr[1], 1))

            if winner != cur_winner:
                streak = 1
                winner = cur_winner
            else:
                streak += 1

            arr.append(arr.pop(1 - i))

        return winner


class Solution1:
    """
    leetcode solution 1: Simulate Process With Queue
    Time: O(n)
    Space: O(n)
    Runtime: 535 ms, faster than 55.43% of Python3 online submissions for Find the Winner of an Array Game.
    Memory Usage: 30.4 MB, less than 17.39% of Python3 online submissions for Find the Winner of an Array Game. 
    """

    def getWinner(self, arr: List[int], k: int) -> int:
        max_element = max(arr)
        queue = deque(arr[1:])
        curr = arr[0]
        winstreak = 0

        while queue:
            opponent = queue.popleft()
            if curr > opponent:
                queue.append(opponent)
                winstreak += 1
            else:
                queue.append(curr)
                curr = opponent
                winstreak = 1

            if winstreak == k or curr == max_element:
                return curr


class Solution2:
    """
    leetcode solution 2: No Queue
    Time: O(n)
    Space: O(1)
    Runtime: 535 ms, faster than 55.43% of Python3 online submissions for Find the Winner of an Array Game.
    Memory Usage: 29.6 MB, less than 85.33% of Python3 online submissions for Find the Winner of an Array Game.
    """

    def getWinner(self, arr: List[int], k: int) -> int:
        max_element = max(arr)
        curr = arr[0]
        winstreak = 0

        for i in range(1, len(arr)):
            opponent = arr[i]
            if curr > opponent:
                winstreak += 1
            else:
                curr = opponent
                winstreak = 1

            if winstreak == k or curr == max_element:
                return curr


s = Solution()
tests = [
    (([2, 1, 3, 5, 4, 6, 7], 2),
     5),

    (([3, 2, 1], 10),
     3),
]
for inp, exp in tests:
    res = s.getWinner(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
