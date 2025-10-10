"""
Leetcode
2025-10-10
3147. Taking Maximum Energy From the Mystic Dungeon
Medium

In a mystic dungeon, n magicians are standing in a line. Each magician has an attribute that gives you energy. Some magicians can give you negative energy, which means taking energy from you.

You have been cursed in such a way that after absorbing energy from magician i, you will be instantly transported to magician (i + k). This process will be repeated until you reach the magician where (i + k) does not exist.

In other words, you will choose a starting point and then teleport with k jumps until you reach the end of the magicians' sequence, absorbing all the energy during the journey.

You are given an array energy and an integer k. Return the maximum possible energy you can gain.

Note that when you are reach a magician, you must take energy from them, whether it is negative or positive energy.

 

Example 1:

Input: energy = [5,2,-10,-5,1], k = 3

Output: 3

Explanation: We can gain a total energy of 3 by starting from magician 1 absorbing 2 + 1 = 3.

Example 2:

Input: energy = [-2,-3,-1], k = 2

Output: -1

Explanation: We can gain a total energy of -1 by starting from magician 2.

 

Constraints:

    1 <= energy.length <= 10^5
    -1000 <= energy[i] <= 1000
    1 <= k <= energy.length - 1


Hint 1
Let dp[i] denote the energy we gain starting from index i.
Hint 2
We can notice, that  dp[i] = dp[i + k] + energy[i].
"""

from math import inf
from typing import List


class Solution:
    """
    Runtime 1201ms Beats 31.25%
    Memory 31.11MB Beats 67.50%
    """

    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        window = [0] * k

        for i in range(0, n, k):
            for j in range(min(k, n - i)):
                window[j] = energy[i + j] + max(window[j], 0)

        return max(window)


class Solution1:
    """
    leetcode solution: Reverse Traversal
    Runtime 1128ms Beats 73.13%
    Memory 31.20MB Beats 55.00%
    """

    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        ans = -inf

        for i in range(n - k, n):
            total = 0
            j = i
            while j >= 0:
                total += energy[j]
                ans = max(ans, total)
                j -= k

        return int(ans)
